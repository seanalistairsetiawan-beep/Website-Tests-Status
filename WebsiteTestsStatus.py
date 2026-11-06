import streamlit as st

st.set_page_config(page_title="Student Grade Calculator", page_icon="🎓")

st.title("🎓 Student Grade Calculator")
st.markdown("Enter the student's name and score to calculate the grade, result, and get a congratulatory message!")

# Input fields
name = st.text_input("Enter Student's Name:", placeholder="e.g., Alex Johnson")
score = st.number_input("Enter Student's Score (0 - 100):", min_value=0.0, max_value=100.0, value=75.0, step=1.0)

# Calculate grade function
def calculate_grade(s):
    if s >= 90:
        return "A"
    elif s >= 80:
        return "B"
    elif s >= 70:
        return "C"
    elif s >= 60:
        return "D"
    else:
      return "F"

# Button to calculate
if st.button("Calculate Grade"):
    if name.strip() == "":
        st.warning("Please enter a valid student name.")
    else:
        grade = calculate_grade(score)
        is_pass = score >= 50.0  # Pass threshold set to 50

        st.divider()
        st.subheader(f"Results for {name}")
        st.metric(label="Score", value=f"{score}")
        st.metric(label="Grade", value=grade)

        if is_pass:
            st.success("Result: **PASS** ✅")
            st.balloons()
            st.markdown(
                f"🎉 **Congratulations, {name}!** You passed the course with a great grade of **{grade}**!"
            )
        else:
            st.error("Result: **FAIL** ❌")
            st.markdown(
                f"Keep your head up, {name}. Review the material and try again!"
            )