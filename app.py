import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from summarizer_chain import get_summary_chain

st.set_page_config(page_title="Text Summarizer", layout="wide")
st.title("📝 Text Summarizer ")

st.markdown("Paste your text below and click **Summarize** to get a concise version.")

text_input = st.text_area("Enter large text here...", height=300)

if st.button("Summarize"):
    if text_input.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        # 1. Split long text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=50
        )
        docs = text_splitter.split_text(text_input)

        with st.spinner("Summarizing..."):
            # 2. Load chain
            chain = get_summary_chain()

            # 3. Run summary on each chunk
            summaries = [chain.run(chunk) for chunk in docs]

            # 4. Join all chunk summaries
            output = "\n\n".join(summaries)

            st.subheader("📌 Summary:")
            st.write(output)
