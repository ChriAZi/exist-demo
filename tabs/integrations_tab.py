import streamlit as st


def render_integrations_tab():
    with st.expander('See explanation'):
        st.write(
            """This section includes all procedural information of the experiment. It enables importing and 
            exporting of information to technical and non-technical tools used for issue management, 
            code versioning, documentation and collaboration. """
        )
    jira, github, confluence, slack, pdf = st.columns(5)
    with jira:
        st.image('https://cdn.icon-icons.com/icons2/2699/PNG/512/atlassian_jira_logo_icon_170511.png',
                 width=50)
        link = '[Open associated JIRA ticket](https://www.atlassian.com/de/software/jira)'
        st.markdown(link, unsafe_allow_html=True)
    with github:
        st.image('https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png',
                 width=50)
        link = '[Open associated Git branch](https://github.com/)'
        st.markdown(link, unsafe_allow_html=True)
    with confluence:
        st.image('https://seeklogo.com/images/C/confluence-logo-D9B07137C2-seeklogo.com.png',
                 width=50)
        link = '[Open technical documentation in Confluence](https://www.atlassian.com/de/software/confluence)'
        st.markdown(link, unsafe_allow_html=True)
    with slack:
        st.image('https://a.slack-edge.com/80588/marketing/img/icons/icon_slack_hash_colored.png',
                 width=50)
        link = '[Share experiment run on Slack](https://slack.com/intl/de-de/)'
        st.markdown(link, unsafe_allow_html=True)
    with pdf:
        st.button('Export model card as PDF')
