import streamlit as st
import json
import os

# ==========================================
# 1. MODEL: DATA & PERSISTENCE LAYER (JSON)
# ==========================================
DB_FILE = "todo_db.json"

def load_database():
    """Disk (JSON) se data volatile memory (List) me load karna"""
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_database(data):
    """Volatile RAM se permanent DISK storage me serialize karna"""
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Streamlit Session State ko initialize karna (RAM simulation)
if "todo_db" not in st.session_state:
    st.session_state.todo_db = load_database()

# ==========================================
# 2. CONTROLLER / LOGIC LAYER
# ==========================================
def add_task_logic(title):
    """Task ko list ke andar dictionary bana kar append karna (O(1))"""
    if not title.strip():
        st.error("❌ Task title khali nahi ho sakta!")
        return False
        
    # Python Dictionary -> Maps to Database Row
    new_task = {
        "title": title.strip(),
        "status": "Pending"
    }
    st.session_state.todo_db.append(new_task)
    save_database(st.session_state.todo_db)
    st.success(f"✅ Task '{title}' safely stored in Database!")
    return True

def toggle_status_logic(index):
    """Task ka status update karna"""
    if st.session_state.todo_db[index]["status"] == "Pending":
        st.session_state.todo_db[index]["status"] = "Completed"
    else:
        st.session_state.todo_db[index]["status"] = "Pending"
    save_database(st.session_state.todo_db)

def delete_task_logic(index):
    """Task ko database se remove karna"""
    st.session_state.todo_db.pop(index)
    save_database(st.session_state.todo_db)

# ==========================================
# 3. VIEW: USER INTERFACE (STREAMLIT)
# ==========================================
st.set_page_config(page_title="DecodeLabs To-Do Engine", page_icon="🚀", layout="centered")

st.title(" DecodeLabs To-Do Engine")
st.caption("Project 1: Advanced Logic & Persistence Phase (In-Memory JSON DB)")
st.write("---")

# IPO Model: INPUT Section
st.subheader(" Data Entry (Input)")
with st.form(key="task_form", clear_on_submit=True):
    task_input = st.text_input("Enter your task title:", placeholder="e.g., Finish Python assignment")
    submit_button = st.form_submit_button(label="Insert Into Database")

if submit_button:
    if add_task_logic(task_input):
        st.rerun()

# IPO Model: OUTPUT Section
st.subheader(" Database View (Output)")

if not st.session_state.todo_db:
    st.info("ℹ In-Memory Database Table is currently empty.")
else:
    # Slide concept: enumerate() ka use kar ke index aur data dono ko render karna
    for index, task in enumerate(st.session_state.todo_db):
        col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
        
        # Task title display with status formatting
        with col1:
            if task["status"] == "Completed":
                st.write(f"~~**{index + 1}.** {task['title']}~~ ✅")
            else:
                st.write(f"**{index + 1}.** {task['title']}")
                
        # Toggle Status button
        with col2:
            btn_label = "Undo" if task["status"] == "Completed" else "Done"
            if st.button(btn_label, key=f"status_{index}"):
                toggle_status_logic(index)
                st.rerun()
                
        # Delete Button
        with col3:
            if st.button("Delete", key=f"del_{index}"):
                delete_task_logic(index)
                st.rerun()

st.write("---")
# Backend State Metrics
st.markdown(f"**Engine Status:** Memory Active | **Total Records:** `{len(st.session_state.todo_db)}` rows")
