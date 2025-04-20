import streamlit as st

st.title('football quiz')

questions = ('who won the ballon dor in 2003:',
             'who is the most player scored goals in the world:',
             'who is the goat:',
             'how many ballon dors did beckenbauer have:',
             'how many champion leagues did ac milan have:',
             'who won the world cup 2014',
             'who won the super ballon dor',
             'the first world cup played in ........')

options = (('A.Ronaldinho','B.Rivaldo','C.Nedved'),
           ('A.Messi','B.Pele','C.Ronaldo'),
           ('ronaldo','B.Messi','C.both'),
           ('A.3','B.4','C.2'),
           ('A.5','B.7','C.6'),
           ('A.germany','B.spain','C.argentina'),
           ('A.Platini','B.de stefano','C.vanpasten'),
           ('A.USA','B.Uruguay','C.Brasil'))


answers = ('C','C','C','C','B','A','B','B')
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.q_index = 0
    st.session_state.guesses = []

if session_state.q_index < len(questions):
    q = questions[st.session_state.q_index]
    opts = options[st.session_state.q_index]
    st.subheader(f'Q{st.session_state.q_index +1}:{q}')
    user_answers = st.radio('choose your answer:',opts)

    if st.button('submit answer'):
        guess_letter = user_answers[0].upper()
        st.session_state.guesses.append(guess_letter)

        if guess_letter == answers[st.session_state.q_index]:
            st.success('correct')
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect! The correct answer was: {answers[st.session_state.q_index]}")
        st.session_state.q_index +=1
        st.rerun()
else:
    st.success(f"🎉 Quiz Completed! Your score: {st.session_state.score}/{len(questions)}")

    if st.button("Restart Quiz"):
        st.session_state.score = 0
        st.session_state.q_index = 0
        st.session_state.guesses = []
        st.rerun()





