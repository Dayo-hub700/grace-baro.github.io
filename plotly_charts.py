import plotly.express as px
import pandas as pd

# If you don't have plotly installed:
# pip install plotly

# assume `master` is your pandas DataFrame already loaded in the environment

# 1) Heatmap of correlations
corr = master[['budget_usd', 'box_office_usd', 'tmdb_rating']].corr()

fig_heatmap = px.imshow(
    corr,
    text_auto='.2f',
    color_continuous_scale='RdBu',
    origin='lower',
    labels=dict(x="Features", y="Features", color="Correlation"),
)

fig_heatmap.update_layout(
    title=dict(text='Heatmap of Budget, Box Office, and TMDB Rating Correlation', x=0.5),
    width=800, height=600,
    font=dict(size=12)
)
# optional: tweak text size
fig_heatmap.update_traces(textfont_size=12)

# Save heatmap
fig_heatmap.write_html("heatmap_correlation.html", include_plotlyjs='cdn', full_html=True)


# 2) Scatter plot: Budget vs Revenue colored by universe
fig_scatter = px.scatter(
    master,
    x='budget_usd',
    y='revenue_usd',
    color='universe',
    hover_data=['title'] if 'title' in master.columns else None,
    labels={'budget_usd': 'Budget (USD)', 'revenue_usd': 'Revenue (USD)', 'universe': 'Universe'},
    title='Plot of Budget vs Revenue'
)

fig_scatter.update_traces(marker=dict(size=10, opacity=0.85, line=dict(width=0.5, color='DarkSlateGrey')))
fig_scatter.update_layout(width=900, height=600, title_x=0.5)

# Save scatter
fig_scatter.write_html("budget_vs_revenue.html", include_plotlyjs='cdn', full_html=True)