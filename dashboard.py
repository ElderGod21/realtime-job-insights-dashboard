#default design

# import pandas as pd
# import streamlit as st

# st.title("Career Insights Dashboard")

# # Load dataset
# @st.cache_data
# def load_data():
#     df = pd.read_csv("data/internshala_jobs.csv", index_col=False)
#     return df

# df = load_data()
# st.subheader("Jobs")
# st.dataframe(df.reset_index(drop=True))
# st.subheader("Key Metrics")
# st.write("Total Jobs:", len(df))
# st.write("Total Companies:", df['Company'].nunique())
# st.write("Job Titles:", df['Job Title'].nunique())

# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)


# Design 2

# import pandas as pd
# import streamlit as st

# st.title("Career Insights Dashboard")

# # Load dataset
# @st.cache_data
# def load_data():
#     df = pd.read_csv("data/internshala_jobs.csv", index_col=False)
#     return df

# df = load_data()

# # Clean and explode skills for filtering
# df['Skills'] = df['Skills'].fillna('')
# df['Skill List'] = df['Skills'].apply(lambda x: [skill.strip() for skill in x.split(',') if skill.strip()])
# all_skills = sorted(set(skill for skills in df['Skill List'] for skill in skills))

# # Streamlit filter
# st.sidebar.header("Filter Jobs")
# selected_skills = st.sidebar.multiselect("Select required skills:", all_skills)

# # Filter DataFrame based on selected skills
# if selected_skills:
#     filtered_df = df[df['Skill List'].apply(lambda skills: all(skill in skills for skill in selected_skills))]
# else:
#     filtered_df = df

# # Show filtered results
# st.subheader("Filtered Jobs")
# st.dataframe(filtered_df.reset_index(drop=True))

# # Key Metrics
# st.subheader("Key Metrics")
# st.write("Total Jobs:", len(filtered_df))
# st.write("Total Companies:", filtered_df['Company'].nunique())
# st.write("Job Titles:", filtered_df['Job Title'].nunique())

# # Demo widget
# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

# Design 3 

# import pandas as pd
# import streamlit as st
# import plotly.express as px

# st.set_page_config(layout="wide")
# st.markdown("<h1 style='text-align: center;'>Career Insights Dashboard</h1>", unsafe_allow_html=True)

# # Load dataset
# @st.cache_data
# def load_data():
#     df = pd.read_csv("data/internshala_jobs.csv", index_col=False)
#     return df

# df = load_data()

# # Clean and preprocess skills
# df['Skills'] = df['Skills'].fillna('')
# df['Skill List'] = df['Skills'].apply(lambda x: [skill.strip() for skill in x.split(',') if skill.strip()])
# all_skills = sorted(set(skill for skills in df['Skill List'] for skill in skills))

# # Show all jobs first
# st.subheader("All Jobs")
# st.dataframe(df.reset_index(drop=True), use_container_width=True)

# # Skill filter (OR logic)
# selected_skills = st.multiselect("🎯 Filter by Skills", all_skills)

# if selected_skills:
#     filtered_df = df[df['Skill List'].apply(lambda skills: any(skill in skills for skill in selected_skills))]
# else:
#     filtered_df = df

# # Pie Chart for job coverage
# st.subheader("📊 Job Coverage Based on Skills")
# pie_df = pd.DataFrame({
#     'Category': ['Matching Jobs', 'Other Jobs'],
#     'Count': [len(filtered_df), len(df) - len(filtered_df)]
# })
# col1, col2 = st.columns([1, 1])
# with col1:
#     pie_chart = px.pie(pie_df, names='Category', values='Count', title='Jobs Matching Your Skills')
#     st.plotly_chart(pie_chart, use_container_width=True)

# # Bar Chart for Top 10 skills in job market
# with col2:
#     skill_counts = pd.Series([skill for skills in df['Skill List'] for skill in skills]).value_counts().head(10)
#     skill_bar_df = pd.DataFrame({'Skill': skill_counts.index, 'Job Count': skill_counts.values})
#     bar_chart = px.bar(skill_bar_df, x='Skill', y='Job Count', title='Top 10 Skills in Demand')
#     st.plotly_chart(bar_chart, use_container_width=True)

# # Display filtered job data
# st.subheader("Filtered Jobs")
# st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)


## Design 4

# import pandas as pd
# import streamlit as st
# import plotly.express as px
# import PyPDF2
# import spacy

# # Inject custom CSS
# st.markdown("""
#     <style>
#     /* Download button color fix */
#     .stDownloadButton>button {
#         background-color: #83c9ff;
#         color: white;
#         border: none;
#         border-radius: 8px;
#         padding: 0.5em 1em;
#     }

#     .stDownloadButton>button:hover {
#         background-color: #31b0d5;
#         color: white;
#     }

#     /* Multiselect / dropdown tags */
#     .st-ds {
#         background-color: #83c9ff !important;
#         color: white !important;
#     }

#     /* Optional: fix spacing or borders if needed */
#     .stMultiSelect .css-1n76uvr {
#         border-radius: 6px !important;
#     }
#     </style>
# """, unsafe_allow_html=True)



# st.set_page_config(layout="wide")
# st.markdown("<h1 style='text-align: center;'>Career Insights Dashboard</h1>", unsafe_allow_html=True)

# # Load and preprocess data
# @st.cache_data
# def load_data():
#     df = pd.read_csv("data/internshala_jobs.csv", index_col=False)
#     df['Skills'] = df['Skills'].fillna('').apply(lambda x: [s.strip() for s in x.split(',') if s.strip()])
#     return df

# df = load_data()

# # Make link clickable
# def make_clickable_link(link):
#     return f'<a href="{link}" target="_blank">View</a>'

# df["Link"] = df["Link"].apply(make_clickable_link)



# # Load spaCy NLP model
# nlp = spacy.load("en_core_web_sm")

# all_skills = sorted({skill for skills in df['Skills'] for skill in skills})
# all_titles = sorted(df["Job Title"].dropna().unique())


# # --- RESUME UPLOAD SECTION ---
# st.subheader("📤 Upload Your Resume (PDF)")

# uploaded_file = st.file_uploader("Upload a PDF Resume", type=["pdf"])
# auto_skills = []
# auto_titles = []

# if uploaded_file:
#     pdf_reader = PyPDF2.PdfReader(uploaded_file)
#     resume_text = ""
#     for page in pdf_reader.pages:
#         resume_text += page.extract_text()

#     st.text_area("📄 Extracted Resume Text", resume_text, height=200)

#     # Process resume using NLP
#     doc = nlp(resume_text.lower())

#     auto_skills = sorted(set([token.text for token in doc if token.text in all_skills]))

#     # Optional: Suggest job titles based on matching job rows
#     matched_rows = df[df['Skills'].apply(lambda skills: any(skill in skills for skill in auto_skills))]
#     auto_titles = sorted(matched_rows['Job Title'].unique().tolist())

#     if auto_skills:
#         st.success(f"✅ Skills found in resume: {', '.join(auto_skills)}")
#     if auto_titles:
#         st.info(f"💼 Suggested job titles: {', '.join(auto_titles)}")


# # Sidebar Filters
# st.subheader("🔍 Filters")


# all_companies = sorted(df["Company"].dropna().unique())
# all_locations = sorted(df["Location"].dropna().unique())
# all_experiences = sorted(df['Experience'].dropna().unique(), key=lambda x: int(x.split()[0]))

# selected_skills = st.multiselect("Select Skills", all_skills, default=auto_skills if auto_skills else None)
# selected_titles = st.multiselect("Select Job Titles", all_titles, default=auto_titles if auto_titles else None)

# company_search = st.multiselect("Search by Company", all_companies)  # keep as single select if OR not needed
# selected_locations = st.multiselect("Select Locations", all_locations)
# selected_experience = st.multiselect("Filter by Experience", all_experiences)

# # Apply filters to main df
# filtered_df = df.copy()

# if selected_skills:
#     filtered_df = filtered_df[filtered_df['Skills'].apply(lambda x: any(skill in x for skill in selected_skills))]

# if selected_titles:
#     filtered_df = filtered_df[filtered_df['Job Title'].isin( selected_titles)]

# if company_search:
#     filtered_df = filtered_df[filtered_df['Company'].isin(company_search)]

# if selected_locations:
#     filtered_df = filtered_df[filtered_df['Location'].isin(selected_locations)]

# if selected_experience:
#     filtered_df = filtered_df[filtered_df['Experience'].isin(selected_experience)]

# # Conditional Title
# title_text = "All Jobs" if not (selected_skills or selected_titles or company_search or selected_locations) else "Filtered Jobs"
# st.subheader(f"📄 {title_text}")

# # Display filtered jobs
# st.write("Click on 'View' in the Link column to open job postings in a new tab.")

# st.markdown(f"### 🧾 Showing {len(filtered_df)} job(s)")


# # Download CSV button
# csv = filtered_df.to_csv(index=False)
# st.download_button("📥 Download CSV", csv, "filtered_jobs.csv", "text/csv")

# # Convert list/set of skills to comma-separated string
# filtered_df['Skills'] = filtered_df['Skills'].apply(lambda x: ', '.join(x) if isinstance(x, (list, set)) else x)


# table_html = filtered_df.reset_index(drop=True).to_html(escape=False, index=False)

# # Inject CSS for layout + scrollable container
# styled_html = f"""
# <style>
#     .scrollable-table {{
#         max-height: 500px;
#         overflow-y: auto;
#         border: 1px solid #ccc;
#     }}
#     table {{
#         table-layout: fixed;
#         width: 100%;
#         word-wrap: break-word;
#         border-collapse: collapse;
#     }}
#     th, td {{
#         padding: 8px;
#         text-align: left;
#         vertical-align: top;
#         border-bottom: 1px solid #ddd;
#     }}
#     td {{
#         max-width: 250px;
#         word-break: break-word;
#     }}
# </style>
# <div class="scrollable-table">{table_html}</div>
# """


# st.write(styled_html, unsafe_allow_html=True)

# # Key Metrics
# st.subheader("📊 Key Metrics")

# col1, col2 = st.columns(2)

# # Pie Chart for job coverage
# pie_df = pd.DataFrame({
#     'Category': ['Matching Jobs', 'Other Jobs'],
#     'Count': [len(filtered_df), len(df) - len(filtered_df)]
# })
# col1, col2 = st.columns([1, 1])
# with col1:
#     pie_chart = px.pie(pie_df, names='Category', values='Count', title='Jobs Matching Your Skills')
#     st.plotly_chart(pie_chart, use_container_width=True)

# # Bar Chart for Top 10 skills in job market
# with col2:
#     skill_counts = pd.Series([skill for skills in df['Skills'] for skill in skills]).value_counts().head(10)
#     skill_bar_df = pd.DataFrame({'Skills': skill_counts.index, 'Job Count': skill_counts.values})
#     bar_chart = px.bar(skill_bar_df, x='Skills', y='Job Count', title='Top 10 Skills in Demand')
#     st.plotly_chart(bar_chart, use_container_width=True)



# #Design 5
# import pandas as pd
# import streamlit as st
# import plotly.express as px
# import PyPDF2
# import re
# from collections import Counter

# # Inject custom CSS
# st.markdown("""
#     <style>
#     /* Download button color fix */
#     .stDownloadButton>button {
#         background-color: #83c9ff;
#         color: white;
#         border: none;
#         border-radius: 8px;
#         padding: 0.5em 1em;
#     }

#     .stDownloadButton>button:hover {
#         background-color: #31b0d5;
#         color: white;
#     }

#     /* Multiselect / dropdown tags */
#     .st-ds {
#         background-color: #83c9ff !important;
#         color: white !important;
#     }
#     </style>
# """, unsafe_allow_html=True)

# st.set_page_config(layout="wide")
# st.markdown("<h1 style='text-align: center;'>Career Insights Dashboard</h1>", unsafe_allow_html=True)

# # --- DATA LOADING AND PREPARATION ---
# @st.cache_data
# def load_data():
#     """Loads and preprocesses the job data from CSV."""
#     df = pd.read_csv("data/internshala_jobs.csv", index_col=False)
#     df['Skills'] = df['Skills'].fillna('').apply(lambda x: [s.strip() for s in str(x).split(',') if s.strip()])
#     # **KEY CHANGE**: We no longer convert the link to HTML here.
#     # The 'Link' column should contain the raw URL.
#     return df

# df = load_data()

# # --- INITIALIZE LISTS AND SESSION STATE ---
# all_skills = sorted(list(set(skill for skills_list in df['Skills'] for skill in skills_list)))
# all_titles = sorted(df["Job Title"].dropna().unique())
# all_companies = sorted(df["Company"].dropna().unique())
# all_locations = sorted(df["Location"].dropna().unique())
# all_experiences = sorted(df['Experience'].dropna().unique(), key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 0) #type: ignore

# # Initialize session state for auto-selected filters
# if 'auto_skills' not in st.session_state:
#     st.session_state.auto_skills = []
# if 'auto_titles' not in st.session_state:
#     st.session_state.auto_titles = []

# # --- RESUME UPLOAD AND SKILL EXTRACTION ---
# st.subheader("📤 Upload Your Resume to Auto-Filter Skills")
# uploaded_file = st.file_uploader("Upload your resume in PDF format", type=["pdf"])

# if uploaded_file:
#     try:
#         pdf_reader = PyPDF2.PdfReader(uploaded_file)
#         resume_text = ""
#         for page in pdf_reader.pages:
#             resume_text += page.extract_text() or ""
        
#         resume_text_lower = resume_text.lower()
#         st.text_area("📄 Extracted Resume Text", resume_text, height=150)

#         # Robust Skill Matching using regex
#         found_skills = []
#         for skill in all_skills:
#             pattern = r'\b' + re.escape(skill.lower()) + r'\b'
#             if re.search(pattern, resume_text_lower):
#                 found_skills.append(skill)
        
#         st.session_state.auto_skills = sorted(list(set(found_skills)))

#         if st.session_state.auto_skills:
#             st.success(f"✅ Skills found in resume: {', '.join(st.session_state.auto_skills)}")
            
#             # Suggest job titles based on matched skills
#             auto_skills_lower = {s.lower() for s in st.session_state.auto_skills}
#             matched_rows = df[df['Skills'].apply(lambda skill_list: any(s.lower() in auto_skills_lower for s in skill_list))]
            
#             if not matched_rows.empty:
#                 st.session_state.auto_titles = sorted(matched_rows['Job Title'].unique().tolist())
#                 st.info(f"💼 Suggested job titles: {', '.join(st.session_state.auto_titles)}")
#             else:
#                  st.session_state.auto_titles = []
#         else:
#             st.warning("No skills from our database were found in your resume.")
#             st.session_state.auto_skills = []
#             st.session_state.auto_titles = []

#     except Exception as e:
#         st.error(f"Error processing PDF file: {e}")
#         st.session_state.auto_skills = []
#         st.session_state.auto_titles = []

# # --- SIDEBAR FILTERS ---
# st.subheader("🔍 Filters")

# selected_skills = st.multiselect("Select Skills", all_skills, default=st.session_state.auto_skills)
# selected_titles = st.multiselect("Select Job Titles", all_titles, default=st.session_state.auto_titles)
# company_search = st.multiselect("Search by Company", all_companies)
# selected_locations = st.multiselect("Select Locations", all_locations)
# selected_experience = st.multiselect("Filter by Experience", all_experiences)

# # --- APPLY FILTERS TO DATAFRAME ---
# filtered_df = df.copy()

# if selected_skills:
#     selected_skills_lower = {s.lower() for s in selected_skills}
#     filtered_df = filtered_df[filtered_df['Skills'].apply(lambda skill_list: any(s.lower() in selected_skills_lower for s in skill_list))]
# if selected_titles:
#     filtered_df = filtered_df[filtered_df['Job Title'].isin(selected_titles)]
# if company_search:
#     filtered_df = filtered_df[filtered_df['Company'].isin(company_search)]
# if selected_locations:
#     filtered_df = filtered_df[filtered_df['Location'].isin(selected_locations)]
# if selected_experience:
#     filtered_df = filtered_df[filtered_df['Experience'].isin(selected_experience)]

# # --- DISPLAY FILTERED JOBS ---
# title_text = "Filtered Jobs" if any([selected_skills, selected_titles, company_search, selected_locations, selected_experience]) else "All Jobs"
# st.subheader(f"📄 {title_text}")
# st.markdown(f"### 🧾 Showing {len(filtered_df)} job(s)")

# # Prepare DataFrame for display
# display_df = filtered_df.copy()
# display_df['Skills'] = display_df['Skills'].apply(lambda x: ', '.join(x))

# # Download button
# csv = display_df.to_csv(index=False)
# st.download_button("📥 Download as CSV", csv, "filtered_jobs.csv", "text/csv")

# # --- KEY CHANGE: Correctly display the link using st.column_config.LinkColumn ---
# st.dataframe(
#     display_df.reset_index(drop=True),
#     column_config={
#         "Link": st.column_config.LinkColumn(
#             "Job Link",  # Sets the header of the column
#             display_text="View"  # The text that will appear as the hyperlink
#         )
#     },
#     use_container_width=True,
#     hide_index=True
# )


# # --- KEY METRICS VISUALIZATIONS ---
# st.subheader("📊 Key Metrics")
# col1, col2 = st.columns(2)

# # Pie Chart for job coverage
# with col1:
#     pie_df = pd.DataFrame({
#         'Category': ['Matching Jobs', 'Other Jobs'],
#         'Count': [len(filtered_df), len(df) - len(filtered_df)]
#     })
#     pie_chart = px.pie(pie_df, names='Category', values='Count', title='Jobs Matching Your Filters', hole = 0.3)
#     st.plotly_chart(pie_chart, use_container_width=True)

# # Bar Chart for Top 10 skills
# with col2:
#     source_df = filtered_df if not filtered_df.empty else df
#     title_suffix = "(Filtered)" if not filtered_df.empty else "(Overall)"
    
#     skill_counts = Counter(skill for skills_list in source_df['Skills'] for skill in skills_list)
#     top_10_skills = skill_counts.most_common(10)
    
#     if top_10_skills:
#         skill_bar_df = pd.DataFrame(top_10_skills, columns=['Skills', 'Job Count'])
#         bar_chart = px.bar(skill_bar_df, x='Skills', y='Job Count', title=f'Top 10 Skills in Demand {title_suffix}')
#         st.plotly_chart(bar_chart, use_container_width=True)
#     else:
#         st.info("No skills data to display for the current selection.")


## Design 6 with varying verical heights of each row
# import pandas as pd
# import streamlit as st
# import plotly.express as px
# import PyPDF2
# import re
# from collections import Counter

# # --- PAGE CONFIG AND STYLING ---
# st.set_page_config(layout="wide")
# st.markdown("<h1 style='text-align: center;'>Career Insights Dashboard</h1>", unsafe_allow_html=True)

# # Inject custom CSS
# st.markdown("""
#     <style>
#     /* Download button color fix */
#     .stDownloadButton>button {
#         background-color: #83c9ff;
#         color: white;
#         border: none;
#         border-radius: 8px;
#         padding: 0.5em 1em;
#     }

#     .stDownloadButton>button:hover {
#         background-color: #31b0d5;
#         color: white;
#     }

#     /* Multiselect / dropdown tags */
#     .st-ds {
#         background-color: #83c9ff !important;
#         color: white !important;
#     }

#     /* --- KEY CHANGE: CSS for Dynamic Row Height --- */
#     /* This rule ensures that long text inside a table cell will wrap. */
#     /* When text wraps, the row's height will automatically increase to fit it. */
#     .stDataFrame td {
#         word-wrap: break-word;
#         vertical-align: top; /* Optional: Aligns content to top, looks better */
#     }
#     </style>
# """, unsafe_allow_html=True)


# # --- DATA LOADING AND PREPARATION ---
# @st.cache_data
# def load_data():
#     """Loads and preprocesses the job data from CSV."""
#     df = pd.read_csv("data/internshala_jobs.csv", index_col=False)
#     df['Skills'] = df['Skills'].fillna('').apply(lambda x: [s.strip() for s in str(x).split(',') if s.strip()])
#     return df

# df = load_data()

# # --- INITIALIZE LISTS AND SESSION STATE ---
# all_skills = sorted(list(set(skill for skills_list in df['Skills'] for skill in skills_list)))
# all_titles = sorted(df["Job Title"].dropna().unique())
# all_companies = sorted(df["Company"].dropna().unique())
# all_locations = sorted(df["Location"].dropna().unique())
# all_experiences = sorted(df['Experience'].dropna().unique(), key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 0) #type: ignore

# # Initialize session state for auto-selected filters
# if 'auto_skills' not in st.session_state:
#     st.session_state.auto_skills = []
# if 'auto_titles' not in st.session_state:
#     st.session_state.auto_titles = []

# # --- RESUME UPLOAD AND SKILL EXTRACTION ---
# st.subheader("📤 Upload Your Resume to Auto-Filter Skills")
# uploaded_file = st.file_uploader("Upload your resume in PDF format", type=["pdf"])

# if uploaded_file:
#     try:
#         pdf_reader = PyPDF2.PdfReader(uploaded_file)
#         resume_text = ""
#         for page in pdf_reader.pages:
#             resume_text += page.extract_text() or ""
        
#         resume_text_lower = resume_text.lower()
#         st.text_area("📄 Extracted Resume Text", resume_text, height=150)

#         # Robust Skill Matching using regex
#         found_skills = []
#         for skill in all_skills:
#             pattern = r'\b' + re.escape(skill.lower()) + r'\b'
#             if re.search(pattern, resume_text_lower):
#                 found_skills.append(skill)
        
#         st.session_state.auto_skills = sorted(list(set(found_skills)))

#         if st.session_state.auto_skills:
#             st.success(f"✅ Skills found in resume: {', '.join(st.session_state.auto_skills)}")
            
#             # Suggest job titles based on matched skills
#             auto_skills_lower = {s.lower() for s in st.session_state.auto_skills}
#             matched_rows = df[df['Skills'].apply(lambda skill_list: any(s.lower() in auto_skills_lower for s in skill_list))]
            
#             if not matched_rows.empty:
#                 st.session_state.auto_titles = sorted(matched_rows['Job Title'].unique().tolist())
#                 st.info(f"💼 Suggested job titles: {', '.join(st.session_state.auto_titles)}")
#             else:
#                  st.session_state.auto_titles = []
#         else:
#             st.warning("No skills from our database were found in your resume.")
#             st.session_state.auto_skills = []
#             st.session_state.auto_titles = []

#     except Exception as e:
#         st.error(f"Error processing PDF file: {e}")
#         st.session_state.auto_skills = []
#         st.session_state.auto_titles = []

# # --- FILTERS ---
# with st.sidebar: 
#     st.subheader("🔍 Filters")

#     selected_skills = st.multiselect("Select Skills", all_skills, default=st.session_state.auto_skills)
#     selected_titles = st.multiselect("Select Job Titles", all_titles, default=st.session_state.auto_titles)
#     company_search = st.multiselect("Search by Company", all_companies)
#     selected_locations = st.multiselect("Select Locations", all_locations)
#     selected_experience = st.multiselect("Filter by Experience", all_experiences)

# # --- APPLY FILTERS TO DATAFRAME ---
# filtered_df = df.copy()

# if selected_skills:
#     selected_skills_lower = {s.lower() for s in selected_skills}
#     filtered_df = filtered_df[filtered_df['Skills'].apply(lambda skill_list: any(s.lower() in selected_skills_lower for s in skill_list))]
# if selected_titles:
#     filtered_df = filtered_df[filtered_df['Job Title'].isin(selected_titles)]
# if company_search:
#     filtered_df = filtered_df[filtered_df['Company'].isin(company_search)]
# if selected_locations:
#     filtered_df = filtered_df[filtered_df['Location'].isin(selected_locations)]
# if selected_experience:
#     filtered_df = filtered_df[filtered_df['Experience'].isin(selected_experience)]

# # --- DISPLAY FILTERED JOBS ---
# # title_text = "Filtered Jobs" if any([selected_skills, selected_titles, company_search, selected_locations, selected_experience]) else "All Jobs"
# # st.subheader(f"📄 {title_text}")
# st.markdown(f"### 🧾 Showing {len(filtered_df)} job(s)")

# # Prepare DataFrame for display
# display_df = filtered_df.copy()
# display_df['Skills'] = display_df['Skills'].apply(lambda x: ', '.join(x))

# # Download button
# csv = display_df.to_csv(index=False)
# st.download_button("📥 Download as CSV", csv, "filtered_jobs.csv", "text/csv")

# # Make link clickable
# def make_clickable_link(link):
#     # This function should already be in your script from previous steps
#     return f'<a href="{link}" target="_blank">View</a>'

# # Apply this function to the 'Link' column
# display_df['Link'] = display_df['Link'].apply(make_clickable_link)

# # Display the table. The injected CSS will handle the row height automatically.
# table_html = display_df.reset_index(drop=True).to_html(escape=False, index=False)

# # --- KEY CHANGE: INJECT CSS WITH SPECIFIC COLUMN WIDTHS ---
# st.markdown("""
#     <style>
#     .scrollable-table {
#         max-height: 600px;
#         overflow-y: auto;
#         border: 1px solid #e6e9ef;
#         border-radius: 8px;
#     }
#     table {
#         width: 100%;
#         table-layout: fixed; /* This is crucial for the widths to work */
#         border-collapse: collapse;
#     }
#     th, td {
#         padding: 8px 12px;
#         text-align: left;
#         vertical-align: top;
#         border-bottom: 1px solid #ddd;
#         word-wrap: break-word; /* Wrap long text */
#         overflow-wrap: break-word;
#     }
#     th {
#         font-weight: bold;         /* Optional: Makes header text bold */
#         text-align: center !important ;        /* This is the rule that centers the text */
#         padding: 8px 12px;
#         vertical-align: top;
#         border-bottom: 1px solid #ddd;
#     }
    
#     /* --- SMART COLUMN WIDTHS --- */
#     /* Assign widths to columns by their position */
#     th:nth-child(1), td:nth-child(1) { width: 14%; }  /* Job Title */
#     th:nth-child(2), td:nth-child(2) { width: 19%; }  /* Company */
#     th:nth-child(3), td:nth-child(3) { width: 26%; }  /* Skills */
#     th:nth-child(4), td:nth-child(4) { width: 10%; }  /* Location */
#     th:nth-child(5), td:nth-child(5) { width: 13%; }  /* Salary */
#     th:nth-child(6), td:nth-child(6) { width: 6%; }  /* Experience */
#     th:nth-child(7), td:nth-child(7) { width: 6%; }  /* Posted */
#     th:nth-child(8), td:nth-child(8) { width: 6%; }  /* Link */

#     </style>
#      """, unsafe_allow_html=True)

# # Render the HTML table inside the styled div
# html_to_render = f'<div class="scrollable-table">{table_html}</div>'
# st.markdown(html_to_render, unsafe_allow_html=True)


# # --- KEY METRICS VISUALIZATIONS ---
# st.subheader("📊 Key Metrics")
# col1, col2 = st.columns(2)

# # Pie Chart for job coverage
# with col1:
#     pie_df = pd.DataFrame({
#         'Category': ['Matching Jobs', 'Other Jobs'],
#         'Count': [len(filtered_df), len(df) - len(filtered_df)]
#     })
#     pie_chart = px.pie(pie_df, names='Category', values='Count', title='Jobs Matching Your Filters', hole=0.3)
#     st.plotly_chart(pie_chart, use_container_width=True)

# # Bar Chart for Top 10 skills
# with col2:
#     source_df = filtered_df if not filtered_df.empty else df
#     title_suffix = "(Filtered)" if not filtered_df.empty else "(Overall)"
    
#     skill_counts = Counter(skill for skills_list in source_df['Skills'] for skill in skills_list)
#     top_10_skills = skill_counts.most_common(10)
    
#     if top_10_skills:
#         skill_bar_df = pd.DataFrame(top_10_skills, columns=['Skills', 'Job Count'])
#         bar_chart = px.bar(skill_bar_df, x='Skills', y='Job Count', title=f'Top 10 Skills in Demand {title_suffix}')
#         st.plotly_chart(bar_chart, use_container_width=True)
#     else:
#         st.info("No skills data to display for the current selection.")


#Design 7
# import pandas as pd
# import streamlit as st
# import plotly.express as px
# import PyPDF2
# import re
# from collections import Counter

# # --- 1. PAGE CONFIG AND INITIALIZATION ---
# st.set_page_config(layout="wide")
# st.markdown("<h1 style='text-align: center;'>Career Insights Dashboard</h1>", unsafe_allow_html=True)


# # --- 2. DATA LOADING ---
# @st.cache_data
# def load_data():
#     """Loads and preprocesses the job data from CSV."""
#     try:
#         df = pd.read_csv("data/internshala_jobs.csv", index_col=False)
#         df['Skills'] = df['Skills'].fillna('').apply(lambda x: [s.strip() for s in str(x).split(',') if s.strip()])
#         return df
#     except FileNotFoundError:
#         st.error("Error: 'data/internshala_jobs.csv' not found. Please make sure the CSV file is in the correct directory.")
#         return pd.DataFrame()

# df = load_data()

# if df.empty:
#     st.stop()


# # --- 3. STATE MANAGEMENT SETUP ---
# filter_keys = ['skills', 'titles', 'companies', 'locations', 'experience']
# for key in filter_keys:
#     if key not in st.session_state:
#         st.session_state[key] = []


# # --- 4. RESUME PROCESSING LOGIC ---
# st.subheader("📤 Upload Your Resume to Auto-Filter Skills")
# uploaded_file = st.file_uploader(
#     "Upload your resume in PDF format to automatically apply skill and job title filters below.",
#     type=["pdf"],
#     label_visibility="collapsed"
# )

# if uploaded_file:
#     current_file_identifier = f"{uploaded_file.name}-{uploaded_file.size}"
#     if current_file_identifier != st.session_state.get('processed_file_identifier'):
#         try:
#             pdf_reader = PyPDF2.PdfReader(uploaded_file)
#             st.session_state.resume_text = "".join(page.extract_text() or "" for page in pdf_reader.pages)
#             resume_text_lower = st.session_state.resume_text.lower()
            
#             all_skills_list = sorted(list(set(skill for sl in df['Skills'] for skill in sl)))
#             found_skills = [skill for skill in all_skills_list if re.search(r'\b' + re.escape(skill.lower()) + r'\b', resume_text_lower)]
            
#             st.session_state.skills = sorted(list(set(found_skills)))
            
#             if st.session_state.skills:
#                 auto_skills_lower = {s.lower() for s in st.session_state.skills}
#                 matched_rows = df[df['Skills'].apply(lambda sl: any(s.lower() in auto_skills_lower for s in sl))]
#                 st.session_state.titles = sorted(matched_rows['Job Title'].unique().tolist()) if not matched_rows.empty else []
#             else:
#                 st.session_state.titles = []
            
#             st.session_state.processed_file_identifier = current_file_identifier
#             st.rerun()

#         except Exception as e:
#             st.error(f"Error processing PDF file: {e}")
#             st.session_state.processed_file_identifier = None


# # --- 5. SIDEBAR FILTERS ---
# with st.sidebar:
#     st.subheader("🔍 Filters")
#     st.multiselect("Select Skills", sorted(list(set(skill for sl in df['Skills'] for skill in sl))), key='skills')
#     st.multiselect("Select Job Titles", sorted(df["Job Title"].dropna().unique()), key='titles')
#     st.multiselect("Search by Company", sorted(df["Company"].dropna().unique()), key='companies')
#     st.multiselect("Select Locations", sorted(df["Location"].dropna().unique()), key='locations')
    
#     all_experiences = sorted(df['Experience'].dropna().unique(), key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 0)
#     st.multiselect("Filter by Experience", all_experiences, key='experience')


# # --- 6. APPLY FILTERS TO DATAFRAME ---
# filtered_df = df.copy()
# if st.session_state.skills:
#     skills_lower = {s.lower() for s in st.session_state.skills}
#     filtered_df = filtered_df[filtered_df['Skills'].apply(lambda sl: any(s.lower() in skills_lower for s in sl))]
# if st.session_state.titles:
#     filtered_df = filtered_df[filtered_df['Job Title'].isin(st.session_state.titles)]
# if st.session_state.companies:
#     filtered_df = filtered_df[filtered_df['Company'].isin(st.session_state.companies)]
# if st.session_state.locations:
#     filtered_df = filtered_df[filtered_df['Location'].isin(st.session_state.locations)]
# if st.session_state.experience:
#     filtered_df = filtered_df[filtered_df['Experience'].isin(st.session_state.experience)]


# # --- 7. CREATE TABBED LAYOUT ---
# tab_board, tab_analytics, tab_resume = st.tabs(["📄 Job Board", "📊 Dashboard Analytics", "💡 Resume Insights"])

# with tab_board:
#     st.markdown(f"### 🧾 Showing {len(filtered_df)} job(s)")
#     display_df = filtered_df.copy()
#     display_df['Skills'] = display_df['Skills'].apply(lambda x: ', '.join(x))
    
#     csv = display_df.to_csv(index=False).encode('utf-8')
#     st.download_button("📥 Download as CSV", csv, "filtered_jobs.csv", "text/csv")
    
#     def make_clickable_link(link): return f'<a href="{link}" target="_blank">View</a>'
#     display_df['Link'] = display_df['Link'].apply(make_clickable_link)
    
#     table_html = display_df.reset_index(drop=True).to_html(escape=False, index=False)
#     html_to_render = f'<div class="scrollable-table">{table_html}</div>'
#     st.markdown(html_to_render, unsafe_allow_html=True)

# with tab_analytics:
#     st.subheader("Key Metrics for Your Filtered View")
#     col1, col2 = st.columns(2)
    
#     with col1:
#         pie_df = pd.DataFrame({'Category': ['Matching Jobs', 'Other Jobs'], 'Count': [len(filtered_df), len(df) - len(filtered_df)]})
#         pie_chart = px.pie(pie_df, names='Category', values='Count', title='Jobs Matching Your Filters', hole=0.3)
#         st.plotly_chart(pie_chart, use_container_width=True)

#     with col2:
#         source_df = filtered_df if not filtered_df.empty else df
#         title_suffix = "(in Filtered Jobs)" if not filtered_df.empty else "(Overall)"
        
#         skill_counts = Counter(skill for skills_list in source_df['Skills'] for skill in skills_list)
#         top_10_skills = skill_counts.most_common(10)
        
#         if top_10_skills:
#             skill_bar_df = pd.DataFrame(top_10_skills, columns=['Skills', 'Job Count'])
#             bar_chart = px.bar(skill_bar_df, x='Skills', y='Job Count', title=f'Top 10 Skills in Demand {title_suffix}')
#             st.plotly_chart(bar_chart, use_container_width=True)
#         else:
#             st.info("No skills data to display for the current selection.")

# with tab_resume:
#     st.subheader("Intelligent Skill Gap Analysis")

#     if not st.session_state.get('resume_text'):
#         st.info("Upload your resume on the main page to generate a skill gap analysis.")
#     elif filtered_df.empty:
#         st.warning("No jobs match your current filters. Adjust the filters in the sidebar to perform a skill gap analysis against relevant jobs.")
#     else:
#         # --- 1. Calculate Skill Frequencies and Define Core Skills ---
#         num_filtered_jobs = len(filtered_df)
#         user_skills = set(s.lower() for s in st.session_state.skills)

#         all_job_skills_flat = [skill.lower() for skills_list in filtered_df['Skills'] for skill in skills_list]
#         required_skill_counts = Counter(all_job_skills_flat)
#         all_required_skills = set(required_skill_counts.keys())

#         # Define a core skill as one that appears in at least 30% of the filtered jobs
#         CORE_SKILL_THRESHOLD = 0.30
#         core_skills = {skill for skill, count in required_skill_counts.items() if (count / num_filtered_jobs) >= CORE_SKILL_THRESHOLD}

#         # --- 2. Determine Skill Categories ---
#         matched_skills = user_skills.intersection(all_required_skills)
#         missing_core_skills = core_skills - user_skills
#         missing_bonus_skills = all_required_skills - user_skills - core_skills

#         # --- 3. Display the Analysis ---
#         st.markdown("This analysis compares the skills from your resume against the skills required by the jobs you've filtered. Focus on the **High-Priority Skills** to become a top candidate.")
#         st.divider()

#         col1, col2 = st.columns(2)

#         with col1:
#             st.markdown("#### ✅ Your Matched Skills")
#             if matched_skills:
#                 st.success(f"You have these required skills: **{', '.join(sorted(list(matched_skills)))}**")
#             else:
#                 st.info("None of your resume skills match the current job filters.")

#         with col2:
#             st.markdown("#### 🎯 High-Priority Skills to Learn")
#             if missing_core_skills:
#                 st.warning(f"Focus on learning these! They appear in over {int(CORE_SKILL_THRESHOLD*100)}% of the filtered jobs: **{', '.join(sorted(list(missing_core_skills)))}**")
#             else:
#                 st.success("Excellent! You have all the high-priority skills for this job selection.")
        
#         st.divider()
#         st.markdown("#### 💡 Other Recommended Skills")
#         if missing_bonus_skills:
#             st.info(f"Consider learning these to broaden your appeal: {', '.join(sorted(list(missing_bonus_skills)))}")
#         else:
#             st.info("No other skills are listed in this job selection.")
# # --- 8. INJECT CSS ---
# st.markdown("""
#     <style>
#     /* Download button color */
#     .stDownloadButton>button {
#         background-color: #83c9ff;
#         color: white;
#         border: none;
#         border-radius: 8px;
#         padding: 0.5em 1em;
#     }
#     .stDownloadButton>button:hover {
#         background-color: #31b0d5;
#         color: white;
#     }

#     /* --- CORRECTED STYLES FOR MULTISELECT WIDGET --- */

#     /* Target the selected item tags to force the blue background color */
#     div[data-testid="stMultiSelect"] .st-ds {
#         background-color: #83c9ff !important;
#         color: white !important;
#         border: none !important;
#         border-radius: 6px !important;
#     }

#     /* Style for the 'x' to deselect a single tag */
#     .st-ds svg {
#         background-color: transparent !important;
#         fill: white !important; /* Make the 'x' symbol white */
#     }

#     /* Target the main clear all (X) and dropdown (v) icons in the input box */
#     div[data-testid="stClearIcon"],
#     div[data-testid="stSelectDropdownIndicator"] {
#         background-color: transparent !important;
#     }
    
#     /* --- CORRECTED STYLES FOR TABLE HEADER --- */

#     .scrollable-table {
#         max-height: 600px;
#         overflow-y: auto;
#         border: 1px solid #e6e9ef;
#         border-radius: 8px;
#     }
#     table {
#         width: 100%;
#         table-layout: fixed;
#         border-collapse: collapse;
#     }
#     th {
#         background-color: #0d1117 !important; /* Black background */
#         color: white !important; /* White text */
#         font-weight: bold;
#         text-align: center !important;
#         padding: 12px 12px;
#         vertical-align: middle;
#         border-bottom: 2px solid #484f58;
#     }
#     td {
#         padding: 8px 12px;
#         text-align: left;
#         vertical-align: top;
#         border-bottom: 1px solid #ddd;
#         word-wrap: break-word;
#         overflow-wrap: break-word;
#     }
    
#     /* Column widths */
#     th:nth-child(1), td:nth-child(1) { width: 14%; }
#     th:nth-child(2), td:nth-child(2) { width: 19%; }
#     th:nth-child(3), td:nth-child(3) { width: 26%; }
#     th:nth-child(4), td:nth-child(4) { width: 10%; }
#     th:child(5), td:nth-child(5) { width: 13%; }
#     th:nth-child(6), td:nth-child(6) { width: 6%; }
#     th:nth-child(7), td:nth-child(7) { width: 8%; }
#     th:nth-child(8), td:nth-child(8) { width: 6%; }
#     </style>
#      """, unsafe_allow_html=True)


## Design 8 - AI RECOMMENDATION (NLP)

# import pandas as pd
# import streamlit as st
# import plotly.express as px
# import PyPDF2
# import re
# from collections import Counter
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np

# # --- 1. PAGE CONFIG AND INITIALIZATION ---
# st.set_page_config(layout="wide")
# st.markdown("<h1 style='text-align: center;'>Career Insights Dashboard</h1>", unsafe_allow_html=True)


# # --- 2. DATA LOADING ---
# @st.cache_data
# def load_data():
#     """Loads and preprocesses the job data from CSV."""
#     try:
#         df = pd.read_csv("data/internshala_jobs.csv", index_col=False)
#         # Ensure skills are always a list of strings
#         df['Skills_list'] = df['Skills'].fillna('').apply(lambda x: [s.strip() for s in str(x).split(',') if s.strip()])
#         # Create a string version for vectorization
#         df['Skills_str'] = df['Skills_list'].apply(lambda x: ' '.join(x))
#         return df
#     except FileNotFoundError:
#         st.error("Error: 'data/internshala_jobs.csv' not found. Please make sure the CSV file is in the correct directory.")
#         return pd.DataFrame()

# df = load_data()

# if df.empty:
#     st.stop()


# # --- 3. AI RECOMMENDATION ENGINE SETUP ---
# @st.cache_resource
# def setup_ai_engine(dataframe):
#     """Pre-computes the TF-IDF matrix for the recommendation engine."""
#     tfidf_vectorizer = TfidfVectorizer(max_features=500, stop_words='english')
#     tfidf_matrix = tfidf_vectorizer.fit_transform(dataframe['Skills_str'])
#     return tfidf_vectorizer, tfidf_matrix

# tfidf_vectorizer, tfidf_matrix = setup_ai_engine(df)


# # --- 4. STATE MANAGEMENT SETUP ---
# filter_keys = ['skills', 'titles', 'companies', 'locations', 'experience']
# for key in filter_keys:
#     if key not in st.session_state:
#         st.session_state[key] = []


# # --- 5. RESUME PROCESSING LOGIC ---
# st.subheader("📤 Upload Your Resume to Auto-Filter Skills")
# uploaded_file = st.file_uploader(
#     "Upload your resume to power the AI skill recommender and auto-apply filters below.",
#     type=["pdf"],
#     label_visibility="collapsed"
# )

# if uploaded_file:
#     current_file_identifier = f"{uploaded_file.name}-{uploaded_file.size}"
#     if current_file_identifier != st.session_state.get('processed_file_identifier'):
#         try:
#             pdf_reader = PyPDF2.PdfReader(uploaded_file)
#             st.session_state.resume_text = "".join(page.extract_text() or "" for page in pdf_reader.pages)
#             resume_text_lower = st.session_state.resume_text.lower()
            
#             all_skills_list = sorted(list(set(skill for sl in df['Skills_list'] for skill in sl)))
#             found_skills = [skill for skill in all_skills_list if re.search(r'\b' + re.escape(skill.lower()) + r'\b', resume_text_lower)]
            
#             st.session_state.skills = sorted(list(set(found_skills)))
            
#             if st.session_state.skills:
#                 auto_skills_lower = {s.lower() for s in st.session_state.skills}
#                 matched_rows = df[df['Skills_list'].apply(lambda sl: any(s.lower() in auto_skills_lower for s in sl))]
#                 st.session_state.titles = sorted(matched_rows['Job Title'].unique().tolist()) if not matched_rows.empty else []
#             else:
#                 st.session_state.titles = []
            
#             st.session_state.processed_file_identifier = current_file_identifier
#             st.rerun()

#         except Exception as e:
#             st.error(f"Error processing PDF file: {e}")
#             st.session_state.processed_file_identifier = None


# # --- 6. SIDEBAR FILTERS ---
# with st.sidebar:
#     st.subheader("🔍 Filters")
#     st.multiselect("Select Skills", sorted(list(set(skill for sl in df['Skills_list'] for skill in sl))), key='skills')
#     st.multiselect("Select Job Titles", sorted(df["Job Title"].dropna().unique()), key='titles')
#     st.multiselect("Search by Company", sorted(df["Company"].dropna().unique()), key='companies')
#     st.multiselect("Select Locations", sorted(df["Location"].dropna().unique()), key='locations')
    
#     all_experiences = sorted(df['Experience'].dropna().unique(), key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 0)
#     st.multiselect("Filter by Experience", all_experiences, key='experience')


# # --- 7. APPLY FILTERS TO DATAFRAME ---
# filtered_df = df.copy()
# if st.session_state.skills:
#     skills_lower = {s.lower() for s in st.session_state.skills}
#     filtered_df = filtered_df[filtered_df['Skills_list'].apply(lambda sl: any(s.lower() in skills_lower for s in sl))]
# if st.session_state.titles:
#     filtered_df = filtered_df[filtered_df['Job Title'].isin(st.session_state.titles)]
# # ... (rest of the filters)
# if st.session_state.companies:
#     filtered_df = filtered_df[filtered_df['Company'].isin(st.session_state.companies)]
# if st.session_state.locations:
#     filtered_df = filtered_df[filtered_df['Location'].isin(st.session_state.locations)]
# if st.session_state.experience:
#     filtered_df = filtered_df[filtered_df['Experience'].isin(st.session_state.experience)]


# # --- 8. CREATE TABBED LAYOUT ---
# tab_board, tab_analytics, tab_resume = st.tabs(["📄 Job Board", "📊 Dashboard Analytics", "🤖 AI Resume Insights"])

# with tab_board:
#     st.markdown(f"### 🧾 Showing {len(filtered_df)} job(s)")
#     display_df = filtered_df.copy()
#     display_df['Skills'] = display_df['Skills_list'].apply(lambda x: ', '.join(x))
    
#     csv = display_df.to_csv(index=False).encode('utf-8')
#     st.download_button("📥 Download as CSV", csv, "filtered_jobs.csv", "text/csv")
    
#     def make_clickable_link(link): return f'<a href="{link}" target="_blank">View</a>'
#     display_df['Link'] = display_df['Link'].apply(make_clickable_link)
    
#     table_html = display_df.drop(columns=['Skills_list', 'Skills_str']).reset_index(drop=True).to_html(escape=False, index=False)
#     html_to_render = f'<div class="scrollable-table">{table_html}</div>'
#     st.markdown(html_to_render, unsafe_allow_html=True)

# with tab_analytics:
#     st.subheader("Key Metrics for Your Filtered View")
#     col1, col2 = st.columns(2)
    
#     with col1:
#         pie_df = pd.DataFrame({'Category': ['Matching Jobs', 'Other Jobs'], 'Count': [len(filtered_df), len(df) - len(filtered_df)]})
#         pie_chart = px.pie(pie_df, names='Category', values='Count', title='Jobs Matching Your Filters', hole=0.3)
#         st.plotly_chart(pie_chart, use_container_width=True)

#     with col2:
#         source_df = filtered_df if not filtered_df.empty else df
#         title_suffix = "(in Filtered Jobs)" if not filtered_df.empty else "(Overall)"
        
#         skill_counts = Counter(skill for skills_list in source_df['Skills_list'] for skill in skills_list)
#         top_10_skills = skill_counts.most_common(10)
        
#         if top_10_skills:
#             skill_bar_df = pd.DataFrame(top_10_skills, columns=['Skills', 'Job Count'])
#             bar_chart = px.bar(skill_bar_df, x='Skills', y='Job Count', title=f'Top 10 Skills in Demand {title_suffix}')
#             st.plotly_chart(bar_chart, use_container_width=True)
#         else:
#             st.info("No skills data to display for the current selection.")


# # --- START: AI-POWERED RESUME INSIGHTS TAB ---
# with tab_resume:
#     st.subheader("🤖 AI-Powered Skill Recommendations")

#     if not st.session_state.get('skills'):
#         st.info("Upload your resume or select skills in the sidebar to generate personalized recommendations.")
#     else:
#         # --- 1. Get User's Skills and Calculate Similarity ---
#         user_skills_str = ' '.join(st.session_state.skills)
#         user_vector = tfidf_vectorizer.transform([user_skills_str])
#         cosine_similarities = cosine_similarity(user_vector, tfidf_matrix).flatten()

#         # --- 2. Identify Top Matching Jobs and Required Skills ---
#         # Get top 10% of jobs, but at least 5
#         num_top_jobs = max(5, int(len(df) * 0.1))
#         top_job_indices = cosine_similarities.argsort()[-num_top_jobs:][::-1]
        
#         top_jobs_df = df.iloc[top_job_indices]
        
#         # --- 3. Find Missing Skills from These Top Jobs ---
#         user_skills_set = set(s.lower() for s in st.session_state.skills)
        
#         skills_from_top_jobs = [skill.lower() for sublist in top_jobs_df['Skills_list'] for skill in sublist]
#         skill_counts_in_top_jobs = Counter(skills_from_top_jobs)

#         missing_skills = {skill for skill in skills_from_top_jobs if skill not in user_skills_set}
        
#         # Rank missing skills by their frequency in the top-matching jobs
#         ranked_missing_skills = sorted(missing_skills, key=lambda skill: skill_counts_in_top_jobs[skill], reverse=True)
        
#         # --- 4. Display the Recommendations ---
#         st.markdown("Based on your current skill set, here are the most valuable skills to learn. Acquiring these will make you a strong candidate for jobs that are already a good match for you.")
#         st.divider()

#         col1, col2 = st.columns([1, 2])

#         with col1:
#             st.markdown("#### ✅ Your Core Skills")
#             st.success(f"**{', '.join(st.session_state.skills)}**")

#         with col2:
#             st.markdown("#### 🎯 AI Recommended Skills")
#             if ranked_missing_skills:
#                 # Use a more visually appealing list
#                 st.warning("Focus on these to maximize your career opportunities:")
#                 for skill in ranked_missing_skills[:10]: # Show top 10 recommendations
#                     st.markdown(f"- **{skill.title()}**")
#             else:
#                 st.success("You have all the skills for the jobs that best match your profile!")
        
#         st.divider()
#         st.markdown("#### ✨ Top Job Titles for You")
#         st.info(f"Your skills are a strong fit for roles like: **{', '.join(top_jobs_df['Job Title'].unique()[:5])}**")


# # # --- 8. INJECT CSS ---
# st.markdown("""
#     <style>
#     /* --- GENERAL STYLES --- */
#     .stDownloadButton>button {
#         background-color: #83c9ff;
#         color: white;
#         border: none;
#         border-radius: 8px;
#         padding: 0.5em 1em;
#     }
#     .stDownloadButton>button:hover {
#         background-color: #0043AB; /* Dark blue hover */
#         color: white;
#     }

#     /* --- NEW, ROBUST MULTISELECT STYLES --- */

#     /* Style for the selected item tags using the stable data-baseweb attribute */
#     span[data-baseweb="tag"] {
#         background-color: #83c9ff !important; /* Light blue background */
#         color: white !important;
#         border: 1px solid #83c9ff !important;
#         border-radius: 6px !important;
#     }

#     /* Hover effect for the tags */
#     span[data-baseweb="tag"]:hover {
#         background-color: #0043AB !important; /* Dark blue hover */
#         border-color: #0043AB !important;
#     }
    
#     /* Style for the 'x' to deselect a single tag */
#     span[data-baseweb="tag"] svg {
#         background-color: transparent !important;
#         fill: white !important; /* Make the 'x' symbol white */
#     }

#     /* Remove background from the main clear all (X) and dropdown (v) icons */
#     div[data-testid="stClearIcon"],
#     div[data-testid="stSelectDropdownIndicator"] {
#         background-color: transparent !important;
#     }
    
#     /* Change the border color of the multiselect box when it's focused */
#     div[data-testid="stMultiSelect"]:focus-within > div > div:first-child {
#         border-color: #0043AB !important; /* Dark blue border */
#         box-shadow: 0 0 0 1px #0043AB !important; /* Optional glow effect */
#     }


#     /* --- TABLE STYLES --- */
#     .scrollable-table {
#         max-height: 600px;
#         overflow-y: auto;
#         border: 1px solid #e6e9ef;
#         border-radius: 8px;
#     }
#     table {
#         width: 100%;
#         table-layout: fixed;
#         border-collapse: collapse;
#     }
#     th {
#         background-color: #0d1117 !important;
#         color: white !important;
#         font-weight: bold;
#         text-align: center !important;
#         padding: 12px;
#         vertical-align: middle;
#         border-bottom: 2px solid #484f58;
#     }
#     td {
#         padding: 8px 12px;
#         text-align: left;
#         vertical-align: top;
#         border-bottom: 1px solid #ddd;
#         word-wrap: break-word;
#     }
#     </style>
# """, unsafe_allow_html=True)

## Design 9


# import pandas as pd
# import streamlit as st
# import plotly.express as px
# import PyPDF2
# import re
# from collections import Counter
# import numpy as np

# # --- 1. ROBUSTLY IMPORT SKLEARN AND SET UP AI ENGINE ---
# SKLEARN_INSTALLED = False
# try:
#     from sklearn.feature_extraction.text import TfidfVectorizer
#     from sklearn.metrics.pairwise import cosine_similarity
#     SKLEARN_INSTALLED = True
# except ImportError:
#     pass

# # --- 2. PAGE CONFIG AND INITIALIZATION ---
# st.set_page_config(layout="wide")
# st.markdown("<h1 style='text-align: center;'>Career Insights Dashboard</h1>", unsafe_allow_html=True)


# # --- 3. DATA LOADING ---

# @st.cache_data
# def load_data():
#     """Loads, cleans, and reshapes the job data for optimal performance."""
#     try:
#         df = pd.read_csv("data/internshala_jobs.csv", index_col=False)

#         # --- 1. Integrated Cleaning Logic ---
#         # Drop rows with critical missing values
#         df.dropna(subset=['Job Title', 'Company', 'Location', 'Salary', 'Experience', 'Posted'], inplace=True)
#         # Ensure 'Skills' column is a string before processing
#         df['Skills'] = df['Skills'].astype(str)
#         df.reset_index(drop=True, inplace=True)

#         # --- 2. High-Performance Reshaping ---
#         df['Skills_list'] = df['Skills'].apply(lambda x: [s.strip() for s in x.split(',') if s.strip()])
#         df['Skills_str'] = df['Skills_list'].apply(lambda x: ' '.join(x))
        
#         # "Explode" the DataFrame for fast skill filtering
#         df_exploded = df.explode('Skills_list').rename(columns={'Skills_list': 'Skill'})
        
#         return df, df_exploded
#     except FileNotFoundError:
#         st.error("Error: 'data/internshala_jobs.csv' not found. Please make sure the CSV is in the right directory.")
#         return pd.DataFrame(), pd.DataFrame()

# # Load the original and the fast-filtering version
# df, df_exploded = load_data()

# if df.empty:
#     st.stop()


# # --- 4. AI RECOMMENDATION ENGINE SETUP ---
# if SKLEARN_INSTALLED:
#     @st.cache_resource
#     def setup_ai_engine(dataframe):
#         """Pre-computes the TF-IDF matrix for the recommendation engine."""
#         tfidf_vectorizer = TfidfVectorizer(max_features=500, stop_words='english')
#         tfidf_matrix = tfidf_vectorizer.fit_transform(dataframe['Skills_str'])
#         return tfidf_vectorizer, tfidf_matrix
    
#     tfidf_vectorizer, tfidf_matrix = setup_ai_engine(df)


# # --- 5. STATE MANAGEMENT SETUP ---
# filter_keys = ['skills', 'titles', 'companies', 'locations', 'experience']
# for key in filter_keys:
#     if key not in st.session_state:
#         st.session_state[key] = []


# # --- 6. RESUME PROCESSING LOGIC ---
# st.subheader("📤 Upload Your Resume to Auto-Filter Skills")
# uploaded_file = st.file_uploader(
#     "Upload your resume to power the AI skill recommender and auto-apply filters below.",
#     type=["pdf"],
#     label_visibility="collapsed"
# )

# if uploaded_file:
#     current_file_identifier = f"{uploaded_file.name}-{uploaded_file.size}"
#     if current_file_identifier != st.session_state.get('processed_file_identifier'):
#         try:
#             pdf_reader = PyPDF2.PdfReader(uploaded_file)
#             st.session_state.resume_text = "".join(page.extract_text() or "" for page in pdf_reader.pages)
#             resume_text_lower = st.session_state.resume_text.lower()
#             all_skills_list = sorted(list(set(skill for sl in df['Skills_list'] for skill in sl)))
#             found_skills = [skill for skill in all_skills_list if re.search(r'\b' + re.escape(skill.lower()) + r'\b', resume_text_lower)]
#             st.session_state.skills = sorted(list(set(found_skills)))
#             if st.session_state.skills:
#                 auto_skills_lower = {s.lower() for s in st.session_state.skills}
#                 matched_rows = df[df['Skills_list'].apply(lambda sl: any(s.lower() in auto_skills_lower for s in sl))]
#                 st.session_state.titles = sorted(matched_rows['Job Title'].unique().tolist()) if not matched_rows.empty else []
#             else:
#                 st.session_state.titles = []
#             st.session_state.processed_file_identifier = current_file_identifier
#             st.rerun()
#         except Exception as e:
#             st.error(f"Error processing PDF file: {e}")
#             st.session_state.processed_file_identifier = None


# # --- 7. SIDEBAR FILTERS ---
# with st.sidebar:
#     st.subheader("🔍 Filters")
#     st.multiselect("Select Skills", sorted(list(set(skill for sl in df['Skills_list'] for skill in sl))), key='skills')
#     st.multiselect("Select Job Titles", sorted(df["Job Title"].dropna().unique()), key='titles')
#     st.multiselect("Search by Company", sorted(df["Company"].dropna().unique()), key='companies')
#     st.multiselect("Select Locations", sorted(df["Location"].dropna().unique()), key='locations')
#     all_experiences = sorted(df['Experience'].dropna().unique(), key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 0)
#     st.multiselect("Filter by Experience", all_experiences, key='experience')

    
# # --- 8. APPLY FILTERS TO DATAFRAME (OPTIMIZED) ---
# filtered_df = df.copy()

# # Fast skill filtering using the exploded DataFrame
# if st.session_state.skills:
#     # Get the indices of jobs that have at least one of the selected skills
#     matching_indices = df_exploded[df_exploded['Skill'].isin(st.session_state.skills)].index.unique()
#     # Filter the original DataFrame using these indices
#     filtered_df = filtered_df.loc[matching_indices]

# # The rest of the filters are already fast and remain the same
# if st.session_state.titles:
#     filtered_df = filtered_df[filtered_df['Job Title'].isin(st.session_state.titles)]
# if st.session_state.companies:
#     filtered_df = filtered_df[filtered_df['Company'].isin(st.session_state.companies)]
# if st.session_state.locations:
#     filtered_df = filtered_df[filtered_df['Location'].isin(st.session_state.locations)]
# if st.session_state.experience:
#     filtered_df = filtered_df[filtered_df['Experience'].isin(st.session_state.experience)]


# # --- 9. CREATE TABBED LAYOUT ---
# tab_board, tab_analytics, tab_resume = st.tabs(["📄 Job Board", "📊 Dashboard Analytics", "🤖 AI Resume Insights"])

# with tab_board:
#     st.markdown(f"### 🧾 Showing {len(filtered_df)} job(s)")
#     display_df = filtered_df.copy()
#     display_df['Skills'] = display_df['Skills_list'].apply(lambda x: ', '.join(x))
#     csv = display_df.to_csv(index=False).encode('utf-8')
#     st.download_button("📥 Download as CSV", csv, "filtered_jobs.csv", "text/csv")
#     def make_clickable_link(link): return f'<a href="{link}" target="_blank">View</a>'
#     display_df['Link'] = display_df['Link'].apply(make_clickable_link)
#     table_df = display_df.drop(columns=['Skills_list', 'Skills_str'], errors='ignore')
#     table_html = table_df.reset_index(drop=True).to_html(escape=False, index=False)
#     st.markdown(f'<div class="scrollable-table">{table_html}</div>', unsafe_allow_html=True)

# with tab_analytics:
#     st.subheader("Key Metrics for Your Filtered View")
#     col1, col2 = st.columns(2)
#     with col1:
#         pie_df = pd.DataFrame({'Category': ['Matching Jobs', 'Other Jobs'], 'Count': [len(filtered_df), len(df) - len(filtered_df)]})
#         pie_chart = px.pie(pie_df, names='Category', values='Count', title='Jobs Matching Your Filters', hole=0.3)
#         st.plotly_chart(pie_chart, use_container_width=True)
#     with col2:
#         source_df = filtered_df if not filtered_df.empty else df
#         title_suffix = "(in Filtered Jobs)" if not filtered_df.empty else "(Overall)"
#         skill_counts = Counter(skill for skills_list in source_df['Skills_list'] for skill in skills_list)
#         top_10_skills = skill_counts.most_common(10)
#         if top_10_skills:
#             skill_bar_df = pd.DataFrame(top_10_skills, columns=['Skills', 'Job Count'])
#             bar_chart = px.bar(skill_bar_df, x='Skills', y='Job Count', title=f'Top 10 Skills in Demand {title_suffix}')
#             st.plotly_chart(bar_chart, use_container_width=True)
#         else:
#             st.info("No skills data to display for the current selection.")

# with tab_resume:
#     st.subheader("🤖 AI-Powered Skill Analysis")

#     if not SKLEARN_INSTALLED:
#         st.warning("The AI Recommendation Engine is disabled because `scikit-learn` is not installed.")
#         st.info("To enable this feature, please stop the app, run the command below in your terminal, and then restart the app:")
#         st.code("pip install scikit-learn", language="bash")
#     elif not st.session_state.get('skills'):
#         st.info("Upload your resume or select skills in the sidebar to generate personalized recommendations.")
#     else:
#         # AI Logic to find recommendations
#         user_skills_str = ' '.join(st.session_state.skills)
#         user_vector = tfidf_vectorizer.transform([user_skills_str])
#         cosine_similarities = cosine_similarity(user_vector, tfidf_matrix).flatten()
#         num_top_jobs = max(5, int(len(df) * 0.1))
#         top_job_indices = cosine_similarities.argsort()[-num_top_jobs:][::-1]
#         top_jobs_df = df.iloc[top_job_indices]
#         user_skills_set = set(s.lower() for s in st.session_state.skills)
#         skills_from_top_jobs = [skill.lower() for sublist in top_jobs_df['Skills_list'] for skill in sublist]
#         skill_counts_in_top_jobs = Counter(skills_from_top_jobs)
#         missing_skills = {skill for skill in skills_from_top_jobs if skill not in user_skills_set}
#         ranked_missing_skills = sorted(missing_skills, key=lambda skill: skill_counts_in_top_jobs[skill], reverse=True)

#         st.markdown("""
#         <div class="ai-intro">
#         Based on your resume, here is a breakdown of your current strengths and a tailored plan to enhance your profile for the job market.
#         </div>
#         """, unsafe_allow_html=True)
        
#         # --- CORRECTED LAYOUT AND LIMITED RECOMMENDATIONS ---
#         core_skills_pills = "".join([f'<span class="skill-pill-user">{skill}</span>' for skill in st.session_state.skills])
        
#         if ranked_missing_skills:
#             # Limit to top 10 recommended skills
#             rec_skills_pills = "".join([f'<span class="skill-pill-rec">{skill.title()}</span>' for skill in ranked_missing_skills[:10]])
#         else:
#             rec_skills_pills = '<span class="skill-pill-success">Excellent! You have all the top skills for jobs matching your profile.</span>'

#         # Create the two-column card layout using pure HTML/CSS to avoid glitches
#         cards_html = f"""
#         <div class="cards-wrapper">
#             <div class="skill-card-container">
#                 <h5>✅ Your Core Skills</h5>
#                 <div class="pills-container">{core_skills_pills}</div>
#             </div>
#             <div class="skill-card-container">
#                 <h5>🎯 AI Recommended Skills to Learn</h5>
#                 <div class="pills-container">{rec_skills_pills}</div>
#             </div>
#         </div>
#         """
#         st.markdown(cards_html, unsafe_allow_html=True)

#         st.divider()

#         st.markdown("<h5>✨ Top Job Titles For You</h5>", unsafe_allow_html=True)
#         st.markdown("Your skills are a strong fit for roles like these:")
        
#         # Limit to top 5 unique job titles
#         top_titles = top_jobs_df['Job Title'].unique()[:5]
#         top_titles_html = "".join([f'<span class="job-title-pill">{title}</span>' for title in top_titles])
#         st.markdown(f'<div class="pills-container" style="margin-top: 10px;">{top_titles_html}</div>', unsafe_allow_html=True)


# # --- 10. INJECT CSS ---
# st.markdown("""
#     <style>
#     /* --- GENERAL STYLES --- */
#     .stDownloadButton>button { background-color: #83c9ff; color: white; border: none; border-radius: 8px; padding: 0.5em 1em; }
#     .stDownloadButton>button:hover { background-color: #0043AB; color: white; }

#     /* --- MULTISELECT WIDGET STYLES --- */
#     span[data-baseweb="tag"] { background-color: #83c9ff !important; color: white !important; border-radius: 6px !important; }
#     span[data-baseweb="tag"]:hover { background-color: #0043AB !important; }
#     span[data-baseweb="tag"] svg { fill: white !important; }
#     div[data-testid="stMultiSelect"] div[data-baseweb="base-input"]:focus-within { border-color: #0043AB !important; box-shadow: 0 0 0 2px #0043AB !important; }

#     /* --- TABS STYLES --- */
#     button[data-testid="stTab"][aria-selected="true"] { color: #0043AB; border-bottom: 2px solid #0043AB; }
#     button[data-testid="stTab"]:hover { color: #0043AB; }

#     /* --- TABLE STYLES --- */
#     .scrollable-table { max-height: 600px; overflow-y: auto; }
#     table { width : 100%; border-collapse: collapse; table-layout: fixed; }
#     th { background-color: #0d1117 !important; color: white !important; text-align: left !important; padding: 12px; word-wrap: break-word; }
#     td { padding: 8px 12px; border-bottom: 1px solid #ddd; word-wrap: break-word; }
#     th:nth-child(1), td:nth-child(1) { width: 15%; } th:nth-child(2), td:nth-child(2) { width: 15%; } th:nth-child(3), td:nth-child(3) { width: 25%; } th:nth-child(4), td:nth-child(4) { width: 10%; }
#     th:nth-child(5), td:nth-child(5) { width: 10%; } th:nth-child(6), td:nth-child(6) { width: 10%; } th:nth-child(7), td:nth-child(7) { width: 10%; } th:nth-child(8), td:nth-child(8) { width: 5%; }

#     /* --- AI INSIGHTS TAB STYLES (CORRECTED) --- */
#     .ai-intro { font-size: 1.1em; text-align: center; color: #b0b0b0; margin-bottom: 20px; }
    
#     /* This flex container replaces st.columns to fix the visual glitch */
#     .cards-wrapper {
#         display: flex;
#         gap: 20px;
#         margin-top: 20px;
#     }
    
#     .skill-card-container {
#         flex: 1; /* Each card takes up equal space */
#         background-color: #0f1116;
#         border: 1px solid #30363d;
#         border-radius: 12px;
#         padding: 20px;
#         min-height: 150px;
#     }
#     .skill-card-container h5 { margin-top: 0; margin-bottom: 15px; font-size: 1.1em; border-bottom: 1px solid #30363d; padding-bottom: 10px; }
#     .pills-container { display: flex; flex-wrap: wrap; gap: 8px; }
    
#     .skill-pill-user { display: inline-block; padding: 6px 14px; background-color: #238636; color: white; border-radius: 16px; font-weight: 500; font-size: 0.9em; }
#     .skill-pill-rec { display: inline-block; padding: 6px 14px; background-color: #fca311; color: #14213d; border-radius: 16px; font-weight: 500; font-size: 0.9em; }
#     .job-title-pill { display: inline-block; padding: 6px 14px; background-color: #1c4b82; color: #ffffff; border-radius: 16px; font-weight: 500; font-size: 0.9em; }
#     .skill-pill-success { display: inline-block; padding: 6px 14px; background-color: #1c4b82; color: white; border-radius: 16px; font-weight: 500; font-size: 0.9em; }
#     </style>
#      """, unsafe_allow_html=True)


## Design 10

import pandas as pd
import streamlit as st
import plotly.express as px
import PyPDF2
import re
from collections import Counter
import numpy as np

# --- 1. ROBUSTLY IMPORT SKLEARN AND SET UP AI ENGINE ---
SKLEARN_INSTALLED = False
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    SKLEARN_INSTALLED = True
except ImportError:
    pass

# --- 2. PAGE CONFIG AND INITIALIZATION ---
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>Career Insights Dashboard</h1>", unsafe_allow_html=True)


# --- 3. OPTIMIZED DATA LOADING & CLEANING ---
@st.cache_data
def load_data():
    """Loads, cleans, de-duplicates, and reshapes the job data for optimal performance."""
    try:
        df = pd.read_csv("data/internshala_jobs.csv", index_col=False)
        df.drop_duplicates(subset=['Job Title', 'Company', 'Location', 'Skills'], keep='first', inplace=True)
        df.dropna(subset=['Job Title', 'Company', 'Location', 'Salary', 'Experience', 'Posted'], inplace=True)
        df['Skills'] = df['Skills'].astype(str)
        df.reset_index(drop=True, inplace=True)
        df['Skills_list'] = df['Skills'].apply(lambda x: [s.strip() for s in x.split(',') if s.strip()])
        df['Skills_str'] = df['Skills_list'].apply(lambda x: ' '.join(x))
        df_exploded = df.explode('Skills_list').rename(columns={'Skills_list': 'Skill'})
        return df, df_exploded
    except FileNotFoundError:
        st.error("Error: 'data/internshala_jobs.csv' not found. Please ensure the CSV is in the data/ directory.")
        return pd.DataFrame(), pd.DataFrame()

df, df_exploded = load_data()

if df.empty:
    st.stop()


# --- 4. AI RECOMMENDATION ENGINE SETUP ---
if SKLEARN_INSTALLED:
    @st.cache_resource
    def setup_ai_engine(dataframe):
        tfidf_vectorizer = TfidfVectorizer(max_features=500, stop_words='english')
        tfidf_matrix = tfidf_vectorizer.fit_transform(dataframe['Skills_str'])
        return tfidf_vectorizer, tfidf_matrix
    
    tfidf_vectorizer, tfidf_matrix = setup_ai_engine(df)


# --- 5. STATE MANAGEMENT SETUP ---
filter_keys = ['skills', 'titles', 'companies', 'locations', 'experience']
for key in filter_keys:
    if key not in st.session_state:
        st.session_state[key] = []
if 'sort_by_company' not in st.session_state:
    st.session_state.sort_by_company = 'none'


# --- 6. RESUME PROCESSING LOGIC ---
st.subheader("📤 Upload Your Resume to Auto-Filter Skills")
uploaded_file = st.file_uploader(
    "Upload your resume to power the AI skill recommender and auto-apply filters below.",
    type=["pdf"],
    label_visibility="collapsed"
)

if uploaded_file:
    current_file_identifier = f"{uploaded_file.name}-{uploaded_file.size}"
    if current_file_identifier != st.session_state.get('processed_file_identifier'):
        try:
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            st.session_state.resume_text = "".join(page.extract_text() or "" for page in pdf_reader.pages)
            resume_text_lower = st.session_state.resume_text.lower()
            all_skills_list = sorted(list(set(skill for sl in df['Skills_list'] for skill in sl)))
            found_skills = [skill for skill in all_skills_list if re.search(r'\b' + re.escape(skill.lower()) + r'\b', resume_text_lower)]
            st.session_state.skills = sorted(list(set(found_skills)))
            if st.session_state.skills:
                auto_skills_lower = {s.lower() for s in st.session_state.skills}
                matched_rows = df[df['Skills_list'].apply(lambda sl: any(s.lower() in auto_skills_lower for s in sl))]
                st.session_state.titles = sorted(matched_rows['Job Title'].unique().tolist()) if not matched_rows.empty else []
            else:
                st.session_state.titles = []
            st.session_state.processed_file_identifier = current_file_identifier
            st.rerun()
        except Exception as e:
            st.error(f"Error processing PDF file: {e}")
            st.session_state.processed_file_identifier = None


# --- 7. SIDEBAR FILTERS ---
with st.sidebar:
    st.subheader("🔍 Filters")
    st.multiselect("Select Skills", sorted(list(set(skill for sl in df['Skills_list'] for skill in sl))), key='skills')
    st.multiselect("Select Job Titles", sorted(df["Job Title"].dropna().unique()), key='titles')
    st.multiselect("Search by Company", sorted(df["Company"].dropna().unique()), key='companies')
    st.multiselect("Select Locations", sorted(df["Location"].dropna().unique()), key='locations')
    all_experiences = sorted(df['Experience'].dropna().unique(), key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 0)
    st.multiselect("Filter by Experience", all_experiences, key='experience')


# --- 8. APPLY FILTERS TO DATAFRAME (OPTIMIZED) ---
filtered_df = df.copy()

if st.session_state.skills:
    matching_indices = df_exploded[df_exploded['Skill'].isin(st.session_state.skills)].index.unique()
    filtered_df = df.loc[matching_indices]
if st.session_state.titles:
    filtered_df = filtered_df[filtered_df['Job Title'].isin(st.session_state.titles)]
if st.session_state.companies:
    filtered_df = filtered_df[filtered_df['Company'].isin(st.session_state.companies)]
if st.session_state.locations:
    filtered_df = filtered_df[filtered_df['Location'].isin(st.session_state.locations)]
if st.session_state.experience:
    filtered_df = filtered_df[filtered_df['Experience'].isin(st.session_state.experience)]


# --- 9. CREATE TABBED LAYOUT ---
tab_board, tab_analytics, tab_resume = st.tabs(["📄 Job Board", "📊 Dashboard Analytics", "🤖 AI Resume Insights"])

with tab_board:
    st.markdown(f"### 🧾 Showing {len(filtered_df)} job(s)")
    display_df = filtered_df.copy()
    display_df['Skills'] = display_df['Skills_list'].apply(lambda x: ', '.join(x))
    
    col1, col2 = st.columns([0.2, 0.8]) # Adjusted column ratio for better button spacing
    
    with col1:
        csv = display_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download as CSV", csv, "filtered_jobs.csv", "text/csv")
    
    with col2:
        sort_clicked = st.button("↕️ Sort by Company")
        if sort_clicked:
            st.session_state.sort_by_company = {'none': 'asc', 'asc': 'desc', 'desc': 'none'}[st.session_state.sort_by_company]

    if st.session_state.sort_by_company == 'asc':
        display_df = display_df.sort_values(by='Company', ascending=True)
        st.info("Sorted by Company: A-Z")
    elif st.session_state.sort_by_company == 'desc':
        display_df = display_df.sort_values(by='Company', ascending=False)
        st.info("Sorted by Company: Z-A")

    def make_clickable_link(link): return f'<a href="{link}" target="_blank">View</a>'
    display_df['Link'] = display_df['Link'].apply(make_clickable_link)
    table_df = display_df.drop(columns=['Skills_list', 'Skills_str'], errors='ignore')
    table_html = table_df.reset_index(drop=True).to_html(escape=False, index=False)
    st.markdown(f'<div class="scrollable-table">{table_html}</div>', unsafe_allow_html=True)


with tab_analytics:
    st.subheader("Key Metrics for Your Filtered View")
    col1, col2 = st.columns(2)
    with col1:
        pie_df = pd.DataFrame({'Category': ['Matching Jobs', 'Other Jobs'], 'Count': [len(filtered_df), len(df) - len(filtered_df)]})
        pie_chart = px.pie(pie_df, names='Category', values='Count', title='Jobs Matching Your Filters', hole=0.3)
        st.plotly_chart(pie_chart, use_container_width=True)
    with col2:
        source_df = filtered_df if not filtered_df.empty else df
        title_suffix = "(in Filtered Jobs)" if not filtered_df.empty else "(Overall)"
        skill_counts = Counter(skill for skills_list in source_df['Skills_list'] for skill in skills_list)
        top_10_skills = skill_counts.most_common(10)
        if top_10_skills:
            skill_bar_df = pd.DataFrame(top_10_skills, columns=['Skills', 'Job Count'])
            bar_chart = px.bar(skill_bar_df, x='Skills', y='Job Count', title=f'Top 10 Skills in Demand {title_suffix}')
            st.plotly_chart(bar_chart, use_container_width=True)
        else:
            st.info("No skills data to display for the current selection.")

with tab_resume:
    st.subheader("🤖 AI-Powered Skill Analysis")

    if not SKLEARN_INSTALLED:
        st.warning("The AI Recommendation Engine is disabled because `scikit-learn` is not installed.")
        st.info("To enable this feature, please stop the app, run `pip install scikit-learn`, and restart.")
    elif not st.session_state.get('skills'):
        st.info("Upload your resume or select skills in the sidebar to generate personalized recommendations.")
    else:
        user_skills_str = ' '.join(st.session_state.skills)
        user_vector = tfidf_vectorizer.transform([user_skills_str])
        cosine_similarities = cosine_similarity(user_vector, tfidf_matrix).flatten()
        num_top_jobs = max(5, int(len(df) * 0.1))
        top_job_indices = cosine_similarities.argsort()[-num_top_jobs:][::-1]
        top_jobs_df = df.iloc[top_job_indices]
        user_skills_set = set(s.lower() for s in st.session_state.skills)
        skills_from_top_jobs = [skill.lower() for sublist in top_jobs_df['Skills_list'] for skill in sublist]
        skill_counts_in_top_jobs = Counter(skills_from_top_jobs)
        missing_skills = {skill for skill in skills_from_top_jobs if skill not in user_skills_set}
        ranked_missing_skills = sorted(missing_skills, key=lambda skill: skill_counts_in_top_jobs[skill], reverse=True)

        st.markdown("""<div class="ai-intro">
        Based on your resume, here is a breakdown of your current strengths and a tailored plan to enhance your profile for the job market.
        </div>""", unsafe_allow_html=True)
        
        core_skills_pills = "".join([f'<span class="skill-pill-user">{skill}</span>' for skill in st.session_state.skills])
        rec_skills_pills = ("".join([f'<span class="skill-pill-rec">{skill.title()}</span>' for skill in ranked_missing_skills[:10]])
                            if ranked_missing_skills 
                            else '<span class="skill-pill-success">Excellent! You have all the top skills for jobs matching your profile.</span>')
        
        cards_html = f"""<div class="cards-wrapper">
            <div class="skill-card-container"><h5>✅ Your Core Skills</h5><div class="pills-container">{core_skills_pills}</div></div>
            <div class="skill-card-container"><h5>🎯 AI Recommended Skills to Learn</h5><div class="pills-container">{rec_skills_pills}</div></div>
        </div>"""
        st.markdown(cards_html, unsafe_allow_html=True)

        st.divider()
        st.markdown("<h5>✨ Top Job Titles For You</h5>", unsafe_allow_html=True)
        st.markdown("Your skills are a strong fit for roles like these:")
        top_titles = top_jobs_df['Job Title'].unique()[:5]
        top_titles_html = "".join([f'<span class="job-title-pill">{title}</span>' for title in top_titles])
        st.markdown(f'<div class="pills-container" style="margin-top: 10px;">{top_titles_html}</div>', unsafe_allow_html=True)


# --- 10. INJECT CSS ---
st.markdown("""
    <style>
    /* --- GENERAL STYLES --- */
    .stDownloadButton>button { 
        background-color: #83c9ff; 
        color: white; 
        border: none; 
        border-radius: 8px; 
        padding: 0.5em 1em; 
    }
    .stDownloadButton>button:hover { 
        background-color: #0043AB; 
        color: white; 
    }
    
    /* --- NEW: STYLE FOR THE SORT BUTTON TO MATCH DOWNLOAD BUTTON --- */
    div[data-testid="stButton"] > button {
        background-color: #83c9ff;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    div[data-testid="stButton"] > button:hover {
        background-color: #0043AB;
        color: white;
        border: none; /* Ensure border doesn't reappear on hover */
    }
    div[data-testid="stButton"] > button:focus {
        background-color: #0043AB;
        color: white;
        box-shadow: none; /* Optional: remove focus ring if desired */
    }

    span[data-baseweb="tag"] { background-color: #83c9ff !important; color: white !important; border-radius: 6px !important; }
    span[data-baseweb="tag"]:hover { background-color: #0043AB !important; }
    span[data-baseweb="tag"] svg { fill: white !important; }
    div[data-testid="stMultiSelect"] div[data-baseweb="base-input"]:focus-within { border-color: #0043AB !important; box-shadow: 0 0 0 2px #0043AB !important; }
    button[data-testid="stTab"][aria-selected="true"] { color: #0043AB; border-bottom: 2px solid #0043AB; }
    button[data-testid="stTab"]:hover { color: #0043AB; }

    /* --- TABLE STYLES --- */
    .scrollable-table { max-height: 600px; overflow-y: auto; }
    table { width : 100%; border-collapse: collapse; table-layout: fixed; }
    th { position: sticky; top: 0; background-color: #0d1117 !important; color: white !important; text-align: left !important; padding: 12px; word-wrap: break-word; z-index: 1;}
    td { padding: 8px 12px; border-bottom: 1px solid #ddd; word-wrap: break-word; }
    tr:hover { background-color: #1a1a2e; }
    th:nth-child(1), td:nth-child(1) { width: 15%; } th:nth-child(2), td:nth-child(2) { width: 15%; } th:nth-child(3), td:nth-child(3) { width: 25%; } th:nth-child(4), td:nth-child(4) { width: 10%; }
    th:nth-child(5), td:nth-child(5) { width: 10%; } th:nth-child(6), td:nth-child(6) { width: 10%; } th:nth-child(7), td:nth-child(7) { width: 10%; } th:nth-child(8), td:nth-child(8) { width: 5%; }

    /* --- AI INSIGHTS TAB STYLES --- */
    .ai-intro { font-size: 1.1em; text-align: center; color: #b0b0b0; margin-bottom: 20px; }
    .cards-wrapper { display: flex; gap: 20px; margin-top: 20px; }
    .skill-card-container { flex: 1; background-color: #0f1116; border: 1px solid #30363d; border-radius: 12px; padding: 20px; min-height: 150px; }
    .skill-card-container h5 { margin-top: 0; margin-bottom: 15px; font-size: 1.1em; border-bottom: 1px solid #30363d; padding-bottom: 10px; }
    .pills-container { display: flex; flex-wrap: wrap; gap: 8px; }
    .skill-pill-user { display: inline-block; padding: 6px 14px; background-color: #238636; color: white; border-radius: 16px; font-weight: 500; font-size: 0.9em; }
    .skill-pill-rec { display: inline-block; padding: 6px 14px; background-color: #fca311; color: #14213d; border-radius: 16px; font-weight: 500; font-size: 0.9em; }
    .job-title-pill { display: inline-block; padding: 6px 14px; background-color: #1c4b82; color: #ffffff; border-radius: 16px; font-weight: 500; font-size: 0.9em; }
    .skill-pill-success { display: inline-block; padding: 6px 14px; background-color: #1c4b82; color: white; border-radius: 16px; font-weight: 500; font-size: 0.9em; }
    </style>
     """, unsafe_allow_html=True)