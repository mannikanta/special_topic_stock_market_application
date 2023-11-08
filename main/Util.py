# import  json
# import streamlit as st
# file1 = open("D://SpecialTopicProject1//resources//data.txt","r")
# data = file1.read()
# # print(data)
#
# try:
#     json_data = json.loads(data)
#     st.subheader("Business day Summary")
#     print(json_data["data"]["longBusinessSummary"])
#     # st.write(json_data["data"]["longBusinessSummary"])
#     # st.text(json_data["data"]["longBusinessSummary"])
#     st.info(json_data["data"]["52WeekChange"])
#     st.subheader("Beta Value")
#     st.text(json_data["data"]["beta"])
# except json.JSONDecodeError:
#     print("the data is invalid")
#
