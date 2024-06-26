import streamlit as st
from hugchat import hugchat
from hugchat.login import Login


def generate_response(prompt_input, email, password):
    sign = Login(email, password)
    cookies = sign.login()
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)


def main():
    st.title('Simple ChatBot')

    with st.sidebar:
        st.title('Login HugChat')
        hf_email = st.text_input('Enter your email:')
        hf_password = st.text_input('Enter your password:', type='password')
        if not (hf_email) and not (hf_password):
            st.warning('Please enter your email and password')
        else:
            st.success('Proceed to entering your prompt message!')

    if "message" not in st.session_state:
        st.session_state.message = [
            {"role": "assistant", "content": "How may I help you?"}]

    for message in st.session_state.message:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input(disabled=not (hf_email) and not (hf_password)):
        st.session_state.message.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    if st.session_state.message[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Assistant is typing..."):
                response = generate_response(prompt, hf_email, hf_password)
                st.write(response)
        message = {"role": "assistant", "content": response}
        st.session_state.message.append(message)


if __name__ == '__main__':
    main()
