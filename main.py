import langchain_helper as lch
import streamlit as st
import textwrap

st.title('Prolific ✍🏻')


predefinedBooks = {
    'Charles Bukowski' : ["Post Office", "Factotum","Women","Ham on Rye","Hollywood","Pulp" ],
    'Fyodor Dostoevsky' : ["Crime and Punishment", "The Brothers Karamazov","Notes from Underground","The Idiot","Demons"],
    'Munshi Premchand' : ["Godan","Gaban","Nirmala","Seva Sadan","Karmabhoomi"],
    'Albert Camus' : ["The Rebel","The Myth of Sisyphus","The Stranger","The Plague","The Fall"],
    'Friedrich Nietzche' : ["Thus Spoke Zarathustra","Beyond Good and Evil","The Birth of Tragedy","On the Genealogy of Morality","Ecce Homo"]
}



user_writer = st.sidebar.selectbox('Which writer\'s style do you want?',['Charles Bukowski','Fyodor Dostoevsky','Friedrich Nietzche','Munshi Premchand','Albert Camus'])
user_topics = st.sidebar.text_area(label='What topics do you want the story to be about?',max_chars= 70)
user_language = st.sidebar.selectbox('In which language do you want to write the story in?',['English','French','Hindi','Russian'])



if user_writer and user_topics and user_language:
    user_book = st.sidebar.selectbox("Which books tone do you want to use?",predefinedBooks[user_writer])
    click_me = st.sidebar.button(label='Create')
    if click_me:
        temp = st.empty()
        temp.write('Writing your story. Please wait 😁')
        response = lch.write_story(user_writer, user_topics, user_book, user_language)
        if response :
            temp.empty()
        st.write(textwrap.fill(response['story'],width=80))
