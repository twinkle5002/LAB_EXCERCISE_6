import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="🎓",
    layout="wide"
)

# Custom Styling (HTML/CSS)
custom_css = """
<style>
    .main-title {
        color: #1E3A8A;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-title {
        color: #4B5563;
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 25px;
    }
    .metric-card {
        background-color: #F3F4F6;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 1. Title and Description
st.markdown('<div class="main-title">🎓 Student Performance Analytics Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Interactive insights into student academic performance, department metrics, and attendance distributions.</div>', unsafe_allow_html=True)

# 2. Load Dataset
@st.cache_data
def load_data():
    return pd.read_csv("student_performance.csv")

try:
    df = load_data()
except FileNotFoundError:
    st.error("Error: `student_performance.csv` file not found. Please make sure the CSV file exists in the same directory.")
    st.stop()

# 3. Sidebar Filters
st.sidebar.header("🔍 Filter Options")

# Department Filter
selected_depts = st.sidebar.multiselect(
    "Select Department(s):",
    options=df["Department"].unique(),
    default=df["Department"].unique()
)

# Semester Filter
selected_sems = st.sidebar.multiselect(
    "Select Semester(s):",
    options=sorted(df["Semester"].unique()),
    default=sorted(df["Semester"].unique())
)

# Attendance Range Filter
min_att, max_att = int(df["Attendance"].min()), int(df["Attendance"].max())
selected_att_range = st.sidebar.slider(
    "Select Attendance Range (%):",
    min_value=min_att,
    max_value=max_att,
    value=(min_att, max_att)
)

# Filter Data
filtered_df = df[
    (df["Department"].isin(selected_depts)) &
    (df["Semester"].isin(selected_sems)) &
    (df["Attendance"].between(selected_att_range[0], selected_att_range[1]))
]

# 4. Data Summary Cards
st.subheader("📊 Key Overview Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Students", value=len(filtered_df))
with col2:
    st.metric(label="Average Marks", value=f"{filtered_df['Marks'].mean():.2f}" if not filtered_df.empty else "N/A")
with col3:
    st.metric(label="Average Attendance", value=f"{filtered_df['Attendance'].mean():.1f}%" if not filtered_df.empty else "N/A")
with col4:
    st.metric(label="Pass Rate (≥ 50 Marks)", value=f"{(filtered_df['Marks'] >= 50).mean()*100:.1f}%" if not filtered_df.empty else "N/A")

st.markdown("---")

# 5. Visualizations Section
st.subheader("📈 Performance Visualizations")

if filtered_df.empty:
    st.warning("No records match the selected filter criteria.")
else:
    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:
        # Bar Chart: Avg Marks by Dept
        dept_marks = filtered_df.groupby("Department")["Marks"].mean().reset_index()
        fig_bar = px.bar(
            dept_marks, x="Department", y="Marks",
            title="Average Marks by Department",
            color="Department", text_auto=".1f",
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with row1_col2:
        # Pie Chart: Semester Distribution
        sem_counts = filtered_df["Semester"].value_counts().reset_index()
        sem_counts.columns = ["Semester", "Count"]
        fig_pie = px.pie(
            sem_counts, names="Semester", values="Count",
            title="Student Distribution across Semesters",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:
        # Histogram: Marks Distribution
        fig_hist = px.histogram(
            filtered_df, x="Marks", nbins=10,
            title="Distribution of Student Marks",
            color_discrete_sequence=['#3B82F6']
        )
        fig_hist.update_layout(yaxis_title="Count")
        st.plotly_chart(fig_hist, use_container_width=True)

    with row2_col2:
        # Scatter Plot: Attendance vs Marks
        fig_scatter = px.scatter(
            filtered_df, x="Attendance", y="Marks",
            color="Department", hover_data=["Name", "Semester"],
            title="Attendance vs. Marks Correlation",
            trendline="ols" if len(filtered_df) > 1 else None
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("---")

# 6. Tabular View & CSV Download
st.subheader("📋 Filtered Dataset")
st.dataframe(filtered_df, use_container_width=True)

# Download CSV Button
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=csv,
    file_name="filtered_student_performance.csv",
    mime="text/csv"
)