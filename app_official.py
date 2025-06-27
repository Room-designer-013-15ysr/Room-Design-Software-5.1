import streamlit as st
from PIL import Image

st.title("🛋️ Room Design App with File Upload")

uploaded_files = st.file_uploader(
    "Upload up to 20 photos of furniture or diagrams:",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if uploaded_files:
    st.write(f"✅ You uploaded {len(uploaded_files)} file(s).")
    for uploaded_file in uploaded_files[:20]:  # limit to 20
        image = Image.open(uploaded_file)
        st.image(image, caption=uploaded_file.name, use_column_width=True)
st.header("📝 Extra Notes")

notes = st.text_area("Add any additional notes here:", placeholder="e.g. Swap rug, mount TV, paint walls navy blue...")

if notes:
    st.success("🧠 Notes saved! (Temporarily)")
    st.write(notes)

