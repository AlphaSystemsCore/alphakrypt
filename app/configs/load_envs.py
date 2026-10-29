from dotenv import load_dotenv
import os

load_dotenv()
#CONNECTION URI
LOCAL_DSN_STRING = os.getenv("LOCAL_DSN_STRING")
MAXIMUM_CONN = int(os.getenv("MAXIMUM_CONN"))
MINIMUM_CONN = int(os.getenv("MINIMUM_CONN"))

