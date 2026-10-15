"""
AI Study & Career Planner for Students
A Streamlit app that provides personalized study roadmaps,
skill gap assessments, and a quick doubt-solver.
"""

import streamlit as st

# ---------------------------------------------------------------------------
# Page configuration (must be the very first Streamlit call)
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Smart Student Advisor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Global data: career domains → subjects, resources, and weekly tasks
# ---------------------------------------------------------------------------

CAREER_DATA = {
    "AI / Data Science": {
        "subjects": [
            "Mathematics (Linear Algebra & Calculus)",
            "Statistics & Probability",
            "Python Programming",
            "Machine Learning Fundamentals",
            "Data Wrangling & Visualization",
            "Deep Learning Basics",
        ],
        "roadmap": [
            {
                "week": 1,
                "theme": "Foundations",
                "milestones": [
                    "Revise linear algebra: vectors, matrices, dot products",
                    "Study probability distributions and Bayes' theorem",
                    "Practice Python: NumPy & Pandas basics",
                ],
                "resources": [
                    ("3Blue1Brown – Essence of Linear Algebra", "https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab"),
                    ("Khan Academy – Statistics", "https://www.khanacademy.org/math/statistics-probability"),
                    ("Python for Everybody – Coursera (audit free)", "https://www.coursera.org/specializations/python"),
                ],
            },
            {
                "week": 2,
                "theme": "Core ML Concepts",
                "milestones": [
                    "Understand supervised vs unsupervised learning",
                    "Implement linear & logistic regression from scratch",
                    "Build your first model with scikit-learn",
                ],
                "resources": [
                    ("Google ML Crash Course", "https://developers.google.com/machine-learning/crash-course"),
                    ("scikit-learn User Guide", "https://scikit-learn.org/stable/user_guide.html"),
                    ("Kaggle Intro to ML", "https://www.kaggle.com/learn/intro-to-machine-learning"),
                ],
            },
            {
                "week": 3,
                "theme": "Data Skills & EDA",
                "milestones": [
                    "Perform full EDA on a real dataset",
                    "Master Matplotlib & Seaborn for storytelling",
                    "Learn feature engineering techniques",
                ],
                "resources": [
                    ("Kaggle – Data Visualization", "https://www.kaggle.com/learn/data-visualization"),
                    ("Pandas Official Docs", "https://pandas.pydata.org/docs/user_guide/index.html"),
                    ("Towards Data Science – EDA Guide", "https://towardsdatascience.com/exploratory-data-analysis-8fc1cb20fd15"),
                ],
            },
            {
                "week": 4,
                "theme": "Deep Learning & Projects",
                "milestones": [
                    "Understand neural networks and backpropagation",
                    "Build a simple image classifier with TensorFlow/Keras",
                    "Publish a complete project on GitHub",
                ],
                "resources": [
                    ("fast.ai – Practical Deep Learning", "https://course.fast.ai/"),
                    ("TensorFlow Tutorials", "https://www.tensorflow.org/tutorials"),
                    ("GitHub Student Developer Pack", "https://education.github.com/pack"),
                ],
            },
        ],
    },
    "Web Development": {
        "subjects": [
            "HTML & CSS",
            "JavaScript Fundamentals",
            "React / Frontend Framework",
            "Node.js / Backend Basics",
            "Databases (SQL & NoSQL)",
            "Version Control (Git)",
        ],
        "roadmap": [
            {
                "week": 1,
                "theme": "HTML, CSS & Git",
                "milestones": [
                    "Build a responsive portfolio page with HTML5 & CSS3",
                    "Learn Flexbox and CSS Grid layouts",
                    "Set up Git and push your first project to GitHub",
                ],
                "resources": [
                    ("freeCodeCamp – Responsive Web Design", "https://www.freecodecamp.org/learn/2022/responsive-web-design/"),
                    ("CSS-Tricks – A Complete Guide to Flexbox", "https://css-tricks.com/snippets/css/a-guide-to-flexbox/"),
                    ("Git & GitHub for Beginners – freeCodeCamp", "https://www.youtube.com/watch?v=RGOj5yH7evk"),
                ],
            },
            {
                "week": 2,
                "theme": "JavaScript Core",
                "milestones": [
                    "Master ES6+: arrow functions, promises, async/await",
                    "Manipulate the DOM dynamically",
                    "Build a small interactive to-do app",
                ],
                "resources": [
                    ("javascript.info – The Modern JS Tutorial", "https://javascript.info/"),
                    ("Eloquent JavaScript (free book)", "https://eloquentjavascript.net/"),
                    ("freeCodeCamp – JS Algorithms & Data Structures", "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/"),
                ],
            },
            {
                "week": 3,
                "theme": "React & Frontend",
                "milestones": [
                    "Understand components, props, and state in React",
                    "Build a multi-page SPA with React Router",
                    "Consume a public REST API and display results",
                ],
                "resources": [
                    ("React Official Docs – Quick Start", "https://react.dev/learn"),
                    ("Scrimba – Learn React for Free", "https://scrimba.com/learn/learnreact"),
                    ("The Odin Project – React Path", "https://www.theodinproject.com/paths/full-stack-javascript"),
                ],
            },
            {
                "week": 4,
                "theme": "Backend & Databases",
                "milestones": [
                    "Build a REST API with Node.js + Express",
                    "Connect to a MongoDB or PostgreSQL database",
                    "Deploy full-stack app on Vercel / Railway",
                ],
                "resources": [
                    ("Node.js Official Docs", "https://nodejs.org/en/docs/"),
                    ("MongoDB University (free)", "https://university.mongodb.com/"),
                    ("Full Stack Open – University of Helsinki", "https://fullstackopen.com/en/"),
                ],
            },
        ],
    },
    "Cloud Computing": {
        "subjects": [
            "Networking Fundamentals",
            "Linux & Command Line",
            "Cloud Concepts (IaaS/PaaS/SaaS)",
            "Containerization (Docker & Kubernetes)",
            "Infrastructure as Code (Terraform)",
            "Security & IAM",
        ],
        "roadmap": [
            {
                "week": 1,
                "theme": "Networking & Linux",
                "milestones": [
                    "Understand TCP/IP, DNS, HTTP/S, and subnetting",
                    "Navigate Linux filesystem and write basic shell scripts",
                    "Set up a free-tier cloud account (AWS / GCP / Azure)",
                ],
                "resources": [
                    ("Professor Messer – CompTIA Network+", "https://www.professormesser.com/network-plus/n10-008/n10-008-video/n10-008-training-course/"),
                    ("Linux Journey (interactive)", "https://linuxjourney.com/"),
                    ("AWS Free Tier", "https://aws.amazon.com/free/"),
                ],
            },
            {
                "week": 2,
                "theme": "Cloud Fundamentals",
                "milestones": [
                    "Deploy a virtual machine and configure security groups",
                    "Use object storage (S3 / GCS / Blob) for static hosting",
                    "Understand managed services: RDS, Lambda, Cloud Run",
                ],
                "resources": [
                    ("AWS Cloud Practitioner Essentials (free)", "https://aws.amazon.com/training/digital/aws-cloud-practitioner-essentials/"),
                    ("Google Cloud Skills Boost", "https://cloudskillsboost.google/"),
                    ("Microsoft Learn – Azure Fundamentals", "https://learn.microsoft.com/en-us/training/paths/azure-fundamentals/"),
                ],
            },
            {
                "week": 3,
                "theme": "Containers & CI/CD",
                "milestones": [
                    "Containerize an app with Docker and push to Docker Hub",
                    "Deploy to Kubernetes using kubectl basics",
                    "Set up a GitHub Actions CI/CD pipeline",
                ],
                "resources": [
                    ("Play with Docker (browser lab)", "https://labs.play-with-docker.com/"),
                    ("Kubernetes.io – Interactive Tutorial", "https://kubernetes.io/docs/tutorials/"),
                    ("GitHub Actions Docs", "https://docs.github.com/en/actions"),
                ],
            },
            {
                "week": 4,
                "theme": "IaC & Security",
                "milestones": [
                    "Provision infrastructure with Terraform",
                    "Implement IAM roles and least-privilege policies",
                    "Prepare for a cloud foundations certification exam",
                ],
                "resources": [
                    ("HashiCorp Learn – Terraform", "https://developer.hashicorp.com/terraform/tutorials"),
                    ("AWS IAM Best Practices", "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"),
                    ("Cloud Guru (free tier)", "https://acloudguru.com/"),
                ],
            },
        ],
    },
    "Civil Services (UPSC / PSC)": {
        "subjects": [
            "Indian History & Culture",
            "Geography (Physical & Human)",
            "Indian Polity & Governance",
            "Economy & Social Development",
            "General Science & Environment",
            "Current Affairs & Ethics",
        ],
        "roadmap": [
            {
                "week": 1,
                "theme": "Static Foundation",
                "milestones": [
                    "Cover NCERT History (Class 6–12) and make concise notes",
                    "Study Indian Geography using NCERT + Atlas",
                    "Begin Polity with M. Laxmikanth (Chapters 1–10)",
                ],
                "resources": [
                    ("NCERT Books (free PDFs)", "https://ncert.nic.in/textbook.php"),
                    ("Drishti IAS – Free Study Material", "https://www.drishtiias.com/"),
                    ("Insights IAS – Prelims 2024 Plan", "https://www.insightsonindia.com/"),
                ],
            },
            {
                "week": 2,
                "theme": "Economy & Science",
                "milestones": [
                    "Study Indian Economy: budget, banking, planning",
                    "Cover Environment & Ecology (Shankar IAS book summary)",
                    "Revise General Science through NCERT Class 8–10",
                ],
                "resources": [
                    ("Economic Survey – Ministry of Finance", "https://www.indiabudget.gov.in/economicsurvey/"),
                    ("ForumIAS – Free Notes", "https://forumias.com/"),
                    ("PIB (Press Information Bureau)", "https://pib.gov.in/"),
                ],
            },
            {
                "week": 3,
                "theme": "Current Affairs & Answer Writing",
                "milestones": [
                    "Read The Hindu / Indian Express daily (1 hour)",
                    "Attempt 10 MCQs per subject daily",
                    "Write 2 GS answer practice questions per day",
                ],
                "resources": [
                    ("The Hindu e-Paper", "https://www.thehindu.com/"),
                    ("Civilsdaily – Current Affairs", "https://www.civilsdaily.com/"),
                    ("UPSC Previous Year Papers", "https://upsc.gov.in/examinations/previous-question-papers"),
                ],
            },
            {
                "week": 4,
                "theme": "Revision & Mock Tests",
                "milestones": [
                    "Complete full-length mock test (100 MCQs in 2 hours)",
                    "Analyse weak areas and revise targeted chapters",
                    "Prepare a one-page summary sheet per subject",
                ],
                "resources": [
                    ("BYJU's Exam Prep – Free Mocks", "https://byjusexamprep.com/"),
                    ("Testbook – UPSC Free Tests", "https://testbook.com/upsc"),
                    ("Vision IAS – Free Test Series", "https://www.visionias.in/"),
                ],
            },
        ],
    },
}

# ---------------------------------------------------------------------------
# Doubt-solver knowledge base: common Q&A patterns per domain
# ---------------------------------------------------------------------------

DOUBT_HINTS = {
    "AI / Data Science": [
        ("gradient descent", "Gradient Descent is an optimization algorithm that iteratively adjusts model parameters to minimize a loss function.\n\n**Steps:**\n1. Initialize weights randomly.\n2. Compute the loss (e.g., Mean Squared Error).\n3. Calculate the gradient (∂Loss/∂weight) using backpropagation.\n4. Update: weight = weight − learning_rate × gradient.\n5. Repeat until convergence.\n\n**Tip:** A high learning rate may overshoot; a low one converges slowly."),
        ("overfitting", "Overfitting happens when a model learns noise from training data and fails to generalize.\n\n**Causes:**\n- Too many parameters relative to data.\n- Training for too many epochs.\n\n**Solutions:**\n1. Add more training data.\n2. Use regularization (L1 / L2).\n3. Apply Dropout layers (in neural nets).\n4. Use cross-validation.\n5. Simplify the model architecture."),
        ("precision recall", "**Precision** = TP / (TP + FP) — how many predicted positives are actually positive.\n**Recall** = TP / (TP + FN) — how many actual positives were caught.\n\n**When to prioritize:**\n- Precision: Spam detection (avoid wrongly flagging legit emails).\n- Recall: Cancer screening (avoid missing real cases).\n- F1-Score balances both."),
    ],
    "Web Development": [
        ("closure", "A **closure** in JavaScript is a function that retains access to its outer lexical scope even after the outer function has returned.\n\n**Steps to understand:**\n1. An inner function is declared inside an outer function.\n2. The inner function references a variable from the outer scope.\n3. When the outer function returns, the inner function 'closes over' that variable.\n\n**Example use-case:** Counter functions, data privacy (module pattern), callback handlers."),
        ("event loop", "The **Event Loop** enables JavaScript's non-blocking I/O despite being single-threaded.\n\n**Order of execution:**\n1. Call Stack — synchronous code runs first.\n2. Web APIs — async tasks (setTimeout, fetch) are offloaded.\n3. Callback Queue — completed async callbacks wait here.\n4. Event Loop — moves callbacks to the Call Stack when it's empty.\n5. Microtask Queue (Promises) runs before the Callback Queue."),
        ("restful api", "A **RESTful API** uses HTTP methods to perform CRUD operations on resources.\n\n**HTTP Verbs:**\n- GET → Read\n- POST → Create\n- PUT/PATCH → Update\n- DELETE → Delete\n\n**Best Practices:**\n1. Use nouns for endpoints (`/users`, not `/getUsers`).\n2. Return proper HTTP status codes (200, 201, 404, 500).\n3. Version your API (`/api/v1/`).\n4. Use JSON for request/response bodies."),
    ],
    "Cloud Computing": [
        ("vpc", "A **Virtual Private Cloud (VPC)** is an isolated network section within a public cloud.\n\n**Key Components:**\n1. **Subnets** — divide the VPC into public and private zones.\n2. **Internet Gateway** — allows public subnet to reach the internet.\n3. **Route Tables** — define traffic routing rules.\n4. **Security Groups** — stateful firewall at the instance level.\n5. **NACLs** — stateless firewall at the subnet level.\n\n**Tip:** Put databases in private subnets; web servers in public subnets."),
        ("iam", "**IAM (Identity and Access Management)** controls who can do what in your cloud.\n\n**Core Concepts:**\n1. **Users** — individual identities.\n2. **Groups** — collection of users sharing policies.\n3. **Roles** — temporary credentials assumed by services or users.\n4. **Policies** — JSON documents defining allowed/denied actions.\n\n**Best Practice:** Follow **Least Privilege** — grant only the permissions needed, nothing more."),
        ("kubernetes pod", "A **Pod** is the smallest deployable unit in Kubernetes, wrapping one or more containers.\n\n**Lifecycle:**\n1. Pending → scheduler assigns a node.\n2. Running → at least one container is running.\n3. Succeeded / Failed → all containers terminated.\n\n**Key Points:**\n- Containers in a pod share the same IP and storage volumes.\n- Pods are ephemeral; use Deployments for self-healing replicas.\n- Expose pods externally via a Service object."),
    ],
    "Civil Services (UPSC / PSC)": [
        ("federalism", "**Federalism** in India describes the constitutional division of power between the Centre and States.\n\n**Key Features:**\n1. Dual government: Union + States.\n2. Three legislative lists: Union, State, and Concurrent (Schedule 7).\n3. Independent judiciary (Supreme Court as arbiter).\n4. Single citizenship.\n\n**Indian Federalism is 'Quasi-Federal'** because:\n- Governor is Centre-appointed.\n- Parliament can alter State boundaries.\n- Emergency provisions centralize power (Art. 352, 356, 360)."),
        ("monetary policy", "**Monetary Policy** is RBI's tool to control money supply and inflation.\n\n**Key Instruments:**\n1. **Repo Rate** — rate at which RBI lends to banks; raising it reduces borrowing.\n2. **CRR (Cash Reserve Ratio)** — % of deposits banks must hold with RBI.\n3. **SLR (Statutory Liquidity Ratio)** — % banks must invest in govt securities.\n4. **Open Market Operations** — buying/selling govt bonds.\n\n**MPC (Monetary Policy Committee)** sets the policy rate every two months."),
        ("sustainable development", "**Sustainable Development** = meeting present needs without compromising future generations (Brundtland Report, 1987).\n\n**Three Pillars:**\n1. Economic Growth\n2. Social Equity\n3. Environmental Protection\n\n**India's Actions:**\n- National Action Plan on Climate Change (NAPCC) — 8 missions.\n- SDG India Index by NITI Aayog.\n- Renewable energy targets (500 GW by 2030).\n- International Solar Alliance (ISA)."),
    ],
}

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def get_confidence_color(score: int) -> str:
    """Return a color label based on confidence score."""
    if score <= 2:
        return "🔴 Needs Work"
    elif score <= 3:
        return "🟡 Developing"
    else:
        return "🟢 Confident"


def render_roadmap(roadmap: list, weekly_hours: int) -> None:
    """Render the 4-week roadmap as expandable cards."""
    daily_hours = round(weekly_hours / 6, 1)  # assume 6 study days/week

    for week_data in roadmap:
        with st.expander(
            f"📅 Week {week_data['week']} — {week_data['theme']}",
            expanded=(week_data["week"] == 1),
        ):
            st.markdown(f"**Daily study target:** ~{daily_hours} hrs/day")

            st.markdown("**🎯 Milestones**")
            for milestone in week_data["milestones"]:
                st.markdown(f"- {milestone}")

            st.markdown("**📚 Recommended Resources**")
            for name, url in week_data["resources"]:
                st.markdown(f"- [{name}]({url})")


def render_skill_gap(subjects: list) -> dict:
    """
    Render interactive confidence sliders for each subject.
    Returns a dict of {subject: score}.
    """
    scores = {}
    cols = st.columns(2)
    for idx, subject in enumerate(subjects):
        with cols[idx % 2]:
            score = st.slider(
                label=subject,
                min_value=1,
                max_value=5,
                value=3,
                help="1 = very weak, 5 = very strong",
                key=f"slider_{subject}",
            )
            scores[subject] = score
    return scores


def solve_doubt(question: str, domain: str) -> str:
    """
    Return a step-by-step answer if a keyword matches the knowledge base.
    Falls back to a structured generic response.
    """
    question_lower = question.lower()
    hints = DOUBT_HINTS.get(domain, [])

    for keyword, answer in hints:
        if keyword in question_lower:
            return answer

    # Generic structured fallback
    return (
        f"**Your Question:** {question}\n\n"
        "I don't have a pre-built answer for this exact topic, but here's a "
        "structured approach to find the answer:\n\n"
        "1. **Break it down** — Identify the core concept being asked.\n"
        "2. **Check the docs** — Look at the official documentation or a reputable textbook.\n"
        "3. **Search targeted** — Use queries like `site:stackoverflow.com` or `site:reddit.com/r/learnpython`.\n"
        "4. **Try an example** — Write a minimal reproducible example to test your understanding.\n"
        "5. **Teach it back** — Explain the concept in your own words; gaps will surface.\n\n"
        f"💡 **Suggested search:** `{question} explained simply` on YouTube or Google."
    )


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

with st.sidebar:
    st.image(
        "https://img.icons8.com/color/96/000000/graduation-cap.png",
        width=72,
    )
    st.title("🎓 Smart Student Advisor")
    st.caption("Your AI-powered study & career planner")

    st.divider()

    # Educational level
    edu_level = st.selectbox(
        "📖 Educational Level",
        options=[
            "High School (9–12)",
            "Undergraduate (1st–2nd Year)",
            "Undergraduate (3rd–4th Year)",
            "Postgraduate",
            "Working Professional",
        ],
        index=1,
    )

    # Career domain
    career_domain = st.selectbox(
        "🚀 Target Career Domain",
        options=list(CAREER_DATA.keys()),
        index=0,
    )

    # Weekly study hours
    weekly_hours = st.slider(
        "⏱️ Weekly Available Study Hours",
        min_value=5,
        max_value=60,
        value=15,
        step=5,
        help="Honest estimate of hours you can commit per week.",
    )

    st.divider()
    st.info(
        "Fill out the **Skill Assessment** tab first, then view your "
        "**Roadmap** and use the **Doubt Solver** when stuck."
    )

# ---------------------------------------------------------------------------
# Main area
# ---------------------------------------------------------------------------

st.title("AI Study & Career Planner for Students")
st.markdown(
    f"**Level:** {edu_level} &nbsp;|&nbsp; "
    f"**Domain:** {career_domain} &nbsp;|&nbsp; "
    f"**Weekly Hours:** {weekly_hours} hrs"
)
st.divider()

# Three tabs
tab_assessment, tab_roadmap, tab_doubts = st.tabs([
    "🧠 Skill Gap Assessment",
    "🗺️ Personalized Roadmap",
    "❓ Doubt Solver",
])

# ── Tab 1: Skill Gap Assessment ─────────────────────────────────────────────
with tab_assessment:
    st.subheader("Rate Your Current Confidence")
    st.markdown(
        "Drag each slider to reflect how confident you feel in that subject. "
        "**1** = very weak, **5** = very strong. "
        "Be honest — this shapes your roadmap!"
    )
    st.markdown("")

    domain_data = CAREER_DATA[career_domain]
    subjects = domain_data["subjects"]

    scores = render_skill_gap(subjects)

    st.divider()

    # Summary table
    st.subheader("📊 Your Skill Snapshot")
    col_a, col_b, col_c = st.columns([3, 1, 2])
    col_a.markdown("**Subject**")
    col_b.markdown("**Score**")
    col_c.markdown("**Status**")

    for subject, score in scores.items():
        c1, c2, c3 = st.columns([3, 1, 2])
        c1.write(subject)
        c2.write(f"{score} / 5")
        c3.write(get_confidence_color(score))

    # Overall readiness
    avg_score = sum(scores.values()) / len(scores)
    st.divider()

    if avg_score >= 4.0:
        readiness_msg = "🌟 You're well-prepared! Your roadmap focuses on advanced & project work."
        readiness_color = "success"
    elif avg_score >= 2.5:
        readiness_msg = "📈 Solid base! Your roadmap will balance review and new concepts."
        readiness_color = "info"
    else:
        readiness_msg = "🔧 You have room to grow — your roadmap starts from fundamentals."
        readiness_color = "warning"

    getattr(st, readiness_color)(f"**Overall Readiness: {avg_score:.1f} / 5.0** — {readiness_msg}")

    # Store scores in session state for roadmap tab
    st.session_state["scores"] = scores
    st.session_state["avg_score"] = avg_score

# ── Tab 2: Personalized Roadmap ─────────────────────────────────────────────
with tab_roadmap:
    st.subheader(f"Your 4-Week Roadmap → {career_domain}")

    avg = st.session_state.get("avg_score", 3.0)
    scores_saved = st.session_state.get("scores", {})

    # Personalised header message
    daily_hrs = round(weekly_hours / 6, 1)
    st.markdown(
        f"Based on **{weekly_hours} hrs/week** (~{daily_hrs} hrs/day, 6 days), "
        f"here is your structured plan. 📌 Adjust pace if needed."
    )

    # Highlight weak areas at the top
    if scores_saved:
        weak = [s for s, v in scores_saved.items() if v <= 2]
        if weak:
            st.warning(
                "⚠️ **Priority focus areas** (confidence ≤ 2): "
                + ", ".join(weak)
            )

    st.markdown("")
    render_roadmap(domain_data["roadmap"], weekly_hours)

    st.divider()
    st.markdown(
        "💡 **Pro tip:** After each week, re-rate your confidence sliders in the "
        "Skill Assessment tab to track growth and adjust your focus."
    )

# ── Tab 3: Doubt Solver ──────────────────────────────────────────────────────
with tab_doubts:
    st.subheader("❓ Quick Doubt Solver")
    st.markdown(
        "Type any concept or question related to your chosen domain and get "
        "a structured, step-by-step breakdown."
    )

    # Sample questions as hints
    hint_questions = {
        "AI / Data Science": [
            "What is gradient descent?",
            "Explain overfitting",
            "Difference between precision and recall",
        ],
        "Web Development": [
            "What is a closure in JavaScript?",
            "How does the event loop work?",
            "What is a RESTful API?",
        ],
        "Cloud Computing": [
            "What is a VPC?",
            "Explain IAM roles",
            "What is a Kubernetes pod?",
        ],
        "Civil Services (UPSC / PSC)": [
            "Explain federalism in India",
            "What is monetary policy?",
            "What is sustainable development?",
        ],
    }

    st.markdown("**💬 Try one of these:**")
    hint_cols = st.columns(3)
    hints = hint_questions.get(career_domain, [])
    for i, hint in enumerate(hints):
        with hint_cols[i % 3]:
            if st.button(hint, key=f"hint_{i}"):
                st.session_state["doubt_input"] = hint

    st.markdown("")

    # Text area pre-filled from hint buttons or manual input
    user_question = st.text_area(
        "Your question:",
        value=st.session_state.get("doubt_input", ""),
        height=100,
        placeholder=f"e.g. What is gradient descent? (Domain: {career_domain})",
        key="doubt_text_area",
    )

    if st.button("🔍 Get Answer", type="primary"):
        if not user_question.strip():
            st.warning("Please enter a question before clicking Get Answer.")
        else:
            with st.spinner("Thinking through the answer..."):
                answer = solve_doubt(user_question.strip(), career_domain)

            st.divider()
            st.markdown("### 📖 Step-by-Step Breakdown")
            st.markdown(answer)

            # Suggest related resources
            st.divider()
            st.markdown("**📚 Dive deeper with Week 1 resources:**")
            for name, url in domain_data["roadmap"][0]["resources"]:
                st.markdown(f"- [{name}]({url})")

    # Clear button
    if st.button("🗑️ Clear", key="clear_doubt"):
        st.session_state["doubt_input"] = ""
        st.rerun()

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption(
    "🎓 Smart Student Advisor · Built with Streamlit · "
    "All resources are free and open-source · Good luck with your studies! 🚀"
)
