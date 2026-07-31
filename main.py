import streamlit as st
import random

st.set_page_config(
    page_title="A Little Surprise 🎁",
    page_icon="🐼",
    layout="wide"
)

# --------------------------
# Session State
# --------------------------
if "page" not in st.session_state:
    st.session_state.page = 1


# --------------------------
# PAGE 1
# --------------------------

if st.session_state.page == 1:

    st.markdown("""
    <style>

    .stApp{
        background: linear-gradient(135deg,#FFF5FB,#FFE8F3,#FFFFFF);
        overflow:hidden;
    }

    /* Floating animation */
    .floating{
        position:fixed;
        font-size:28px;
        animation:float 12s linear infinite;
        opacity:0.7;
        pointer-events:none;
        z-index:999;
    }

    @keyframes float{

        0%{
            transform:translateY(110vh) rotate(0deg);
            opacity:0;
        }

        10%{
            opacity:1;
        }

        100%{
            transform:translateY(-20vh) rotate(360deg);
            opacity:0;
        }
    }

    .f1{left:5%;animation-delay:0s;}
    .f2{left:18%;animation-delay:2s;}
    .f3{left:32%;animation-delay:4s;}
    .f4{left:48%;animation-delay:1s;}
    .f5{left:62%;animation-delay:6s;}
    .f6{left:76%;animation-delay:3s;}
    .f7{left:90%;animation-delay:5s;}

    </style>

    <div class="floating f1">🌸</div>
    <div class="floating f2">✨</div>
    <div class="floating f3">💖</div>
    <div class="floating f4">🦋</div>
    <div class="floating f5">🤍</div>
    <div class="floating f6">🌸</div>
    <div class="floating f7">✨</div>

    """, unsafe_allow_html=True)

    st.markdown(
        """
        <h1 style="text-align:center;
        font-size:60px;
        color:#ff4d88;">
        ✨ Hey Krushna Kayande✨
        </h1>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p style="text-align:center;
        font-size:24px;
        color:#444;">
        A little surprise just for you 🤍
        </p>
        """,
        unsafe_allow_html=True,
    )

    left, center, right = st.columns([1,2,1])

    with center:
        st.image("helo.gif", use_container_width=False)

    st.markdown(
        """
        <h2 style="text-align:center;color:#ff66a3;">
        Are you ready? 👀
        </h2>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    left, center, right = st.columns([1,2,1])

    with center:
        if st.button("💖 YES, OPEN IT 💖", use_container_width=True):
            st.session_state.page = 2
            st.rerun()

    st.write("")

    left, center, right = st.columns([1,2,1])

    with center:
        if st.button("🙈 Maybe Later", use_container_width=True):
            st.image("why animation.gif", use_container_width=False)
            st.success("😂Then wait until you not click on the yes button 💕" \
            "\n click on yes button ")



# --------------------------
# PAGE 2
# --------------------------

elif st.session_state.page == 2:

    st.markdown("""
    <style>

    .stApp{
        background: linear-gradient(135deg,#FFF5FB,#FFE8F3,#FFFFFF);
        overflow:hidden;
    }

    /* Make all text BLACK */
    h1,h2,h3,h4,h5,h6,
    p,div,span,label{
        color:#000000 !important;
    }

    .stMarkdown{
        color:#000000 !important;
    }

    /* Info box text */
    div[data-testid="stAlert"] *{
        color:#000000 !important;
    }

    /* Floating animation */
    .floating{
        position:fixed;
        font-size:28px;
        animation:float 12s linear infinite;
        opacity:0.7;
        pointer-events:none;
        z-index:999;
    }

    @keyframes float{

        0%{
            transform:translateY(110vh) rotate(0deg);
            opacity:0;
        }

        10%{
            opacity:1;
        }

        100%{
            transform:translateY(-20vh) rotate(360deg);
            opacity:0;
        }
    }

    .f1{left:5%;animation-delay:0s;}
    .f2{left:18%;animation-delay:2s;}
    .f3{left:32%;animation-delay:4s;}
    .f4{left:48%;animation-delay:1s;}
    .f5{left:62%;animation-delay:6s;}
    .f6{left:76%;animation-delay:3s;}
    .f7{left:90%;animation-delay:5s;}

    </style>

    <div class="floating f1">🌸</div>
    <div class="floating f2">✨</div>
    <div class="floating f3">💖</div>
    <div class="floating f4">🦋</div>
    <div class="floating f5">🤍</div>
    <div class="floating f6">🌸</div>
    <div class="floating f7">✨</div>

    """, unsafe_allow_html=True)

    st.title("📸 Memories with you 📸")

    st.image("cutest.gif", width=180)

    col1, col2, col3, col4, col5, col6 = st.columns(6, gap="large")

    with col1:
        st.image("IMG20250504150611.jpg", use_container_width=True)
        st.markdown("🌸 Koradi Trip")
        st.write("*Every picture with you became a memory I'll always cherish. 💖*")

    with col2:
        st.image("ewdfdg.jpg", use_container_width=True)
        st.markdown("💖movement of love")
        st.write("*Some moments stay in the heart forever, and this is one of them. ✨🤍*")

    with col3:
        st.image("IMG20250222154728.jpg", use_container_width=True)
        st.markdown("✨ Beautiful Day")
        st.write("A memory I'll always keep safe.")

    with col4:
        st.image("IMG-20260127-WA0256.jpg", use_container_width=True)
        st.markdown("💖 Special Moment")
        st.write("The moment I fell for you.")

    with col5:
        st.image("IMG-20260128-WA0225.jpg", use_container_width=True)
        st.markdown("🌷 Great Time")
        st.write("*A simple day, a beautiful memory, and my favourite smile. 😊💙*")

    with col6:
        st.image("IMG-20260130-WA0066(1).jpg", use_container_width=True)
        st.markdown("🤍 Last Memory")
        st.write("*No matter how much time passes, this memory will always make me smile. 🌸💕*")

    st.divider()

    st.info("I just wanted to take a moment to express how much you mean to me 💞🤍.")

    if st.button("Next ➜"):
        st.session_state.page = 3
        st.rerun()



# --------------------------
# PAGE 3
# --------------------------

elif st.session_state.page==3:
    st.markdown("""
        <style>
    
        .stApp{
            background: linear-gradient(135deg,#FFF5FB,#FFE8F3,#FFFFFF);
            overflow:hidden;
        }
        /* Make all text BLACK */
            h1,h2,h3,h4,h5,h6,
            p,div,span,label{
                color:#000000 !important;
                }
    
        /* Floating animation */
        .floating{
            position:fixed;
            font-size:28px;
            animation:float 12s linear infinite;
            opacity:0.7;
            pointer-events:none;
            z-index:999;
        }
    
        @keyframes float{
    
            0%{
                transform:translateY(110vh) rotate(0deg);
                opacity:0;
            }
    
            10%{
                opacity:1;
            }
    
            100%{
                transform:translateY(-20vh) rotate(360deg);
                opacity:0;
            }
        }
    
        .f1{left:5%;animation-delay:0s;}
        .f2{left:18%;animation-delay:2s;}
        .f3{left:32%;animation-delay:4s;}
        .f4{left:48%;animation-delay:1s;}
        .f5{left:62%;animation-delay:6s;}
        .f6{left:76%;animation-delay:3s;}
        .f7{left:90%;animation-delay:5s;}
    
        </style>
    
        <div class="floating f1">🌸</div>
        <div class="floating f2">✨</div>
        <div class="floating f3">💖</div>
        <div class="floating f4">🦋</div>
        <div class="floating f5">🤍</div>
        <div class="floating f6">🌸</div>
        <div class="floating f7">✨</div>
    
        """, unsafe_allow_html=True)
    

    st.title("💌 A Few Things I Want To Say")

    st.image("bday.gif",width=180,use_container_width=False)

    st.write("""

💌 A Letter For You 🤍

Dear Krushna, 🌸

Happy Birthday to one of the most amazing person in my life! 🎂🥳

Today is all about celebrating you. 💖 I hope this new year of your life brings endless happiness, success, peace, and countless beautiful memories. ✨🌈

Thank you for every laugh 😂, every conversation ☕, every silly moment 🤭, and every memory we've created together. Those little moments may seem ordinary, but they mean so much to me. 🤍

You are not just my best friend—you are someone I truly appreciate. 🌻 Your kindness, support, and the way you make people smile make you special. 💫

Life will keep changing, and we'll both get busy with our own journeys. 🌍 But I hope our friendship always stays just as genuine as like before. 💕 Distance may change many things, but I hope it never changes the respect and memories we share. 🌸

Whenever life feels difficult, remember this:
You are stronger than you think. 💪
You are capable of amazing things. 🌟
Never stop believing in yourself. 🌈

Keep smiling 😊,
keep dreaming 💭,
keep growing 🌱,
and keep being the wonderful person you are. 🤍

Thank you for being part of my life. I'm really grateful for all the memories we've made together. 📸✨

I hope this little website brought a smile to your face. 😊💌
    """)

    messages=[
        "🌸 Thank you for always being yourself.",
        "🐼 You're one of my favourite humans.",
        "✨ Keep smiling because it looks good on you.",
        "🌈 Never stop chasing your dreams."
    ]

    if st.button("One More Thing 💕"):
        st.success(random.choice(messages))

    if st.button("Final Surprise 🎁"):
        st.session_state.page=4
        st.rerun()



# --------------------------
# PAGE 4
# --------------------------

elif st.session_state.page==4:
    st.markdown("""
        <style>
    
        .stApp{
            background: linear-gradient(135deg,#FFF5FB,#FFE8F3,#FFFFFF);
            overflow:hidden;
        }
        /* Make all text BLACK */
            h1,h2,h3,h4,h5,h6,
            p,div,span,label{
                color:#000000 !important;
                }
    
        /* Floating animation */
        .floating{
            position:fixed;
            font-size:28px;
            animation:float 12s linear infinite;
            opacity:0.7;
            pointer-events:none;
            z-index:999;
        }
    
        @keyframes float{
    
            0%{
                transform:translateY(110vh) rotate(0deg);
                opacity:0;
            }
    
            10%{
                opacity:1;
            }
    
            100%{
                transform:translateY(-20vh) rotate(360deg);
                opacity:0;
            }
        }
    
        .f1{left:5%;animation-delay:0s;}
        .f2{left:18%;animation-delay:2s;}
        .f3{left:32%;animation-delay:4s;}
        .f4{left:48%;animation-delay:1s;}
        .f5{left:62%;animation-delay:6s;}
        .f6{left:76%;animation-delay:3s;}
        .f7{left:90%;animation-delay:5s;}
    
        </style>
    
        <div class="floating f1">🌸</div>
        <div class="floating f2">✨</div>
        <div class="floating f3">💖</div>
        <div class="floating f4">🦋</div>
        <div class="floating f5">🤍</div>
        <div class="floating f6">🌸</div>
        <div class="floating f7">✨</div>
    
        """, unsafe_allow_html=True)
    

    st.balloons()

    st.title("🎂 HAPPY BIRTHDAY KRUSHNA 🎂")

    st.image("IMG-20260123-WA0051(2).jpg",width=250,use_container_width=False)

    st.markdown(
        """
Once again...

🎉 Happy Birthday, Krushna! 🎂🎈

May this year be filled with love ❤️, laughter 😂, success 🏆, good health 🌿, and happiness every single day. 🌸

Always wishing the very best for you. 🤍✨

No matter how much our lives have changed, my wishes for you never will. I sincerely hope you stay healthy, achieve every dream you work for, and always find happiness wherever life takes you. Happy Birthday.

you are always that cute one krushna for me!

(01001001 00100000 01101100 01101111 01110110 01100101 00100000 01111001 01101111 01110101)
Decode me :)

tiny hint:
"A little secret for the curious mind... 💻🤍"

may be leave it it's better decison !
Even if I'm no longer an important part of your life, 
thank you for visiting my little surprise. Happy Birthday! 🌸 
Take care, always. 🤍

"""
    )

    if st.button("Restart Surprise ❤️"):
        st.session_state.page=1
        st.rerun()
