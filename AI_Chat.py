import streamlit as st
import pandas as pd
import db
from langchain.agents import AgentType
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI

conn = db.create_connection(r'/Users/tomfenemore/PycharmProjects/SailDB/local_sql.db')
df = pd.read_sql_query('SELECT * FROM Training WHERE Debrief=1', conn)
# st.header('Chat with me')
# st.dataframe(df)
# prompt = st.chat_input()

# st.chat_message('user').write(prompt)
# st.chat_message('assistant').write(prompt)
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

if "messages" not in st.session_state or st.sidebar.button("Clear conversation history"):
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="What is this data about?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    llm = ChatOpenAI(
        temperature=0, model="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True
    )

    pandas_df_agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        handle_parsing_errors=True,
    )

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = pandas_df_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)

# def page():
#     conn = db.create_connection(r'/Users/tomfenemore/PycharmProjects/SailDB/local_sql.db')
#     df = pd.read_sql_query('SELECT * FROM Training WHERE Debrief=1', conn)
#     # st.header('Chat with me')
#     # st.dataframe(df)
#     # prompt = st.chat_input()

#     # st.chat_message('user').write(prompt)
#     # st.chat_message('assistant').write(prompt)
#     openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

#     if "messages" not in st.session_state or st.sidebar.button("Clear conversation history"):
#         st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

#     for msg in st.session_state.messages:
#         st.chat_message(msg["role"]).write(msg["content"])

#     if prompt := st.chat_input(placeholder="What is this data about?"):
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         st.chat_message("user").write(prompt)

#         if not openai_api_key:
#             st.info("Please add your OpenAI API key to continue.")
#             st.stop()

#         llm = ChatOpenAI(
#             temperature=0, model="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True
#         )

#         pandas_df_agent = create_pandas_dataframe_agent(
#             llm,
#             df,
#             verbose=True,
#             agent_type=AgentType.OPENAI_FUNCTIONS,
#             handle_parsing_errors=True,
#         )

#         with st.chat_message("assistant"):
#             st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
#             response = pandas_df_agent.run(st.session_state.messages, callbacks=[st_cb])
#             st.session_state.messages.append({"role": "assistant", "content": response})
#             st.write(response)