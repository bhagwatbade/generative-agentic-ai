import os
import re

from dotenv import load_dotenv
from supabase import create_client

import importlib
ChatGoogleGenerativeAI = importlib.import_module("langchain_google_genai").ChatGoogleGenerativeAI

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)

from langchain_core.chat_history import (
    BaseChatMessageHistory
)

from langchain_core.messages import (
    message_to_dict,
    messages_from_dict
)

from langchain_core.runnables.history import (
    RunnableWithMessageHistory
)

def get_ai_response_text(content):

    if isinstance(content, str):
        return content.strip()

    if isinstance(content, list):

        text_parts = []

        for item in content:

            if isinstance(item, str):
                text_parts.append(item)

            elif isinstance(item, dict) and item.get("type") == "text":
                text = item.get("text", "")
                if text:
                    text_parts.append(text)

        if text_parts:
            return "\n".join(part.strip() for part in text_parts if part.strip())

    return str(content).strip()

# ========================================
# 1. SUPABASE CONFIGURATION
# ========================================

load_dotenv()


supabase = create_client(
    os.environ["SUPABASE_URL"],
    os.environ["SUPABASE_SECRET_KEY"]
)


USERS_TABLE = "users"

HISTORY_TABLE = "chat_history"


# ========================================
# 2. LOAD USERS
# ========================================

def load_users():

    response = (
        supabase
        .table(USERS_TABLE)
        .select(
            "username, profile"
        )
        .execute()
    )


    users = {}


    for row in response.data:

        users[
            row["username"]
        ] = row["profile"]


    return users


# ========================================
# 3. SAVE USERS
# ========================================

def save_users(users):

    rows = []


    for username, profile in users.items():

        rows.append(
            {
                "username": username,
                "profile": profile
            }
        )


    if rows:

        (
            supabase
            .table(USERS_TABLE)
            .upsert(
                rows,
                on_conflict="username"
            )
            .execute()
        )


# ========================================
# 4. USER SIGNUP
# ========================================

def signup(users):

    print("\n--- SIGNUP ---")


    name = input(
        "Enter Name: "
    ).strip()


    username = input(
        "Enter Username: "
    ).strip().lower()


    password = input(
        "Enter Password: "
    )


    # ------------------------------------
    # VALIDATE EMPTY VALUES
    # ------------------------------------

    if not name or not username or not password:

        print(
            "All fields are required"
        )

        return


    # ------------------------------------
    # VALIDATE USERNAME
    # ------------------------------------

    if not re.fullmatch(
            r"[a-z0-9_]+",
            username
    ):

        print(
            "Use only letters, "
            "numbers and underscores"
        )

        return


    # ------------------------------------
    # CHECK EXISTING USER
    # ------------------------------------

    if username in users:

        print(
            "Username already exists"
        )

        return


    # ------------------------------------
    # ADD USER
    # ------------------------------------

    users[username] = {
        "name": name,
        "password": password
    }


    # ------------------------------------
    # SAVE TO SUPABASE DATABASE
    # ------------------------------------

    save_users(
        users
    )


    print(
        "Signup Successful!"
    )


# ========================================
# 5. USER LOGIN
# ========================================

def login(users):

    print("\n--- LOGIN ---")


    username = input(
        "Enter Username: "
    ).strip().lower()


    password = input(
        "Enter Password: "
    )


    # ------------------------------------
    # CHECK USERNAME
    # ------------------------------------

    if username not in users:

        print(
            "Invalid Username"
        )

        return None


    # ------------------------------------
    # CHECK PASSWORD
    # ------------------------------------

    if (
            users[username]["password"]
            == password
    ):

        print(
            "Login Successful!"
        )


        print(
            "Welcome",
            users[username]["name"]
        )


        return username


    print(
        "Incorrect Password"
    )


    return None


# ========================================
# 6. SUPABASE DATABASE CHAT HISTORY
# ========================================

class SupabaseChatMessageHistory(
    BaseChatMessageHistory
):


    def __init__(
            self,
            session_id
    ):

        self.session_id = (
            session_id
        )


    # ------------------------------------
    # READ CHAT HISTORY
    # ------------------------------------

    @property
    def messages(self):

        response = (
            supabase
            .table(HISTORY_TABLE)
            .select(
                "messages"
            )
            .eq(
                "session_id",
                self.session_id
            )
            .execute()
        )


        # --------------------------------
        # NEW SESSION
        # --------------------------------

        if not response.data:

            return []


        data = (
            response.data[0]
            ["messages"]
        )


        if not data:

            return []


        return messages_from_dict(
            data
        )


    # ------------------------------------
    # SAVE CHAT HISTORY
    # ------------------------------------

    def add_messages(
            self,
            messages
    ):

        # --------------------------------
        # LOAD EXISTING MESSAGES
        # --------------------------------

        all_messages = (
                self.messages
                + messages
        )


        # --------------------------------
        # LANGCHAIN MESSAGE
        #       ↓
        # PYTHON DICTIONARY
        # --------------------------------

        data = [

            message_to_dict(
                message
            )

            for message
            in all_messages

        ]


        # --------------------------------
        # SAVE JSONB TO SUPABASE
        # --------------------------------

        (
            supabase
            .table(HISTORY_TABLE)
            .upsert(
                {
                    "session_id":
                        self.session_id,

                    "messages":
                        data
                },

                on_conflict=
                "session_id"
            )
            .execute()
        )


    # ------------------------------------
    # CLEAR CHAT HISTORY
    # ------------------------------------

    def clear(self):

        (
            supabase
            .table(HISTORY_TABLE)
            .upsert(
                {
                    "session_id":
                        self.session_id,

                    "messages":
                        []
                },

                on_conflict=
                "session_id"
            )
            .execute()
        )


# ========================================
# 7. CREATE OPENAI MODEL
# ========================================

llm = ChatGoogleGenerativeAI(
    model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite"),
    google_api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY"),
)



# ========================================
# 8. CREATE PROMPT
# ========================================

prompt = (
    ChatPromptTemplate
    .from_messages(
        [

            (
                "system",

                "You are a helpful AI assistant. "
                "Answer in simple English. "
                "The user's name is {name}."
            ),


            MessagesPlaceholder(
                "history"
            ),


            (
                "human",
                "{question}"
            )

        ]
    )
)


# ========================================
# 9. CREATE LCEL CHAIN
# ========================================

chain = (
        prompt
        | llm
)


# ========================================
# 10. GET SESSION HISTORY
# ========================================

def get_session_history(
        session_id
):

    return (
        SupabaseChatMessageHistory(
            session_id
        )
    )


# ========================================
# 11. CREATE CHATBOT WITH HISTORY
# ========================================

chatbot = RunnableWithMessageHistory(

    chain,

    get_session_history,

    input_messages_key=
    "question",

    history_messages_key=
    "history"
)


# ========================================
# 12. LOAD REGISTERED USERS
# ========================================

users = load_users()


current_user = None


# ========================================
# 13. START APPLICATION
# ========================================

print(
    "\nMULTI-USER AI CHATBOT"
)

print(
    "SUPABASE JSONB DATABASE"
)


while True:


    # ====================================
    # USER NOT LOGGED IN
    # ====================================

    if current_user is None:


        print(
            "\n1. Signup"
        )

        print(
            "2. Login"
        )

        print(
            "3. Exit"
        )


        choice = input(
            "Enter Choice: "
        )


        # --------------------------------
        # SIGNUP
        # --------------------------------

        if choice == "1":

            signup(
                users
            )


        # --------------------------------
        # LOGIN
        # --------------------------------

        elif choice == "2":

            current_user = login(
                users
            )


        # --------------------------------
        # EXIT
        # --------------------------------

        elif choice == "3":

            break


        else:

            print(
                "Invalid Choice"
            )


    # ====================================
    # USER LOGGED IN
    # ====================================

    else:


        question = input(
            f"\n{current_user}: "
        ).strip()


        # --------------------------------
        # LOGOUT
        # --------------------------------

        if (
                question.lower()
                == "logout"
        ):

            print(
                "Logged Out"
            )

            current_user = None


        # --------------------------------
        # EXIT
        # --------------------------------

        elif (
                question.lower()
                == "exit"
        ):

            break


        # --------------------------------
        # CHAT
        # --------------------------------

        elif question:


            name = (
                users[
                    current_user
                ]["name"]
            )


            try:

                response = (
                    chatbot.invoke(

                        {
                            "name":
                                name,

                            "question":
                                question
                        },


                        config={
                            "configurable": {

                                "session_id":
                                    current_user

                            }
                        }

                    )
                )


                print("\nAI:", get_ai_response_text(response.content))


            except Exception as error:

                print(
                    "Error:",
                    error
                )


print(
    "\nProgram Ended"
)