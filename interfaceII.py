import streamlit as st
import deploy

# Page configuration
st.set_page_config(
    page_title="IoMT Security Simulator",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Simulate Attack", "Preemptive Analysis"])

# Sample prompts
sample_prompts = [
    "My insulin pump has been working fine, but lately, I've noticed Traffic was observed with the following characteristics: Header length of 36043.6 bytes, using the 6.0 protocol. The connection duration was 64.0 seconds with a rate of 1.3366900608925942 bytes per second, and source rate 1.3366900608925942 bytes per second. The packet contains 0.0 SYN flags, 0.0 RST flags, and 1.0 ACK flags. The SYN packet count is 0.0, FIN packet count is 0.0, and RST packet count is 466.5. TCP traffic is present (1.0), UDP traffic is present (0.0), ICMP traffic is present (0.0), IPv traffic is present (1.0), and LLC traffic is present (1.0). Statistical measures include a total sum of 413.7, minimum value of 66.0, maximum value of 85.8, average of 74.4020238095238, standard deviation of 9.176143913768222, total size of 76.3 bytes, inter-arrival time of 7.359981536865234e-05 microseconds, number of packets 5.5, magnitude 12.1959306758997, radius 12.97702717313835, covariance 93.66396697845803, variance 0.9, and weight 38.5.. I'm not sure if it's just a glitch, but it's making me anxious. What should I do?"]
    #"I've been using my glucose meter regularly, but recently Traffic was observed with the following characteristics: Header length of 356048.3 bytes, using the 8.2 protocol. The connection duration was 76.8 seconds with a rate of 1.334679565536096 bytes per second, and source rate 1.334679565536096 bytes per second. The packet contains 0.0 SYN flags, 0.0 RST flags, and 0.8 ACK flags. The SYN packet count is 0.0, FIN packet count is 0.0, and RST packet count is 4502.2. TCP traffic is present (0.8), UDP traffic is present (0.2), ICMP traffic is present (0.0), IPv traffic is present (1.0), and LLC traffic is present (1.0). Statistical measures include a total sum of 1296.9, minimum value of 66.0, maximum value of 165.0, average of 83.0904316289146, standard deviation of 25.640625144609448, total size of 93.9 bytes, inter-arrival time of 169469820.74475488 microseconds, number of packets 13.5, magnitude 12.895585826009292, radius 36.36121493553036, covariance 808.829354449484, variance 1.0, and weight 244.6.. It’s been functioning normally otherwise, but this seems off. Should I be worried?",
    # "I've been using my connected thermometer regularly, but recently Traffic was observed with the following characteristics: Header length of 11918.0 bytes, using the 17.0 protocol. The connection duration was 64.0 seconds with a rate of 30564.314299118832 bytes per second, and source rate 30564.314299118832 bytes per second. The packet contains 0.0 SYN flags, 0.0 RST flags, and 0.0 ACK flags. The SYN packet count is 0.0, FIN packet count is 0.0, and RST packet count is 0.0. TCP traffic is present (0.0), UDP traffic is present (1.0), ICMP traffic is present (0.0), IPv traffic is present (1.0), and LLC traffic is present (1.0). Statistical measures include a total sum of 525.0, minimum value of 50.0, maximum value of 50.0, average of 50.0, standard deviation of 0.0, total size of 50.0 bytes, inter-arrival time of 84696898.3914884 microseconds, number of packets 9.5, magnitude 10.0, radius 0.0, covariance 0.0, variance 0.0, and weight 141.55.. It’s been functioning normally otherwise, but this seems off. Should I be worried?"
# ]

# Home page
if page == "Home":
    st.title("IoMT Security Simulator")
    st.write(
        """
        Welcome to the IoMT Security Simulator! This tool helps simulate attacks on IoMT devices and provides
        preemptive analysis to mitigate potential security threats.
        Use the navigation on the left to explore different functionalities.
        """
    )

# Simulate Attack page
elif page == "Simulate Attack":
    st.title("Simulate Attack")
    st.write("Enter the kind of attack you would like to simulate.")

    # Display sample prompts
    st.write("### Sample Prompts")
    selected_prompt = st.radio("Choose a sample prompt to use:", sample_prompts)

    if st.button("Use Sample Prompt"):
        st.session_state.attack_description = selected_prompt

    # Use st.text_area with session_state to handle pre-filled text
    attack_description = st.text_area(
        "Attack Description",
        value=st.session_state.get('attack_description', ''),
        placeholder="Describe the attack scenario here..."
    )

    if st.button("Simulate"):
        if attack_description.strip():  # Check if the text area is not empty
            simulation_result = deploy.simulate(attack_description)
            st.write("### Simulation Steps")
            st.write(simulation_result)
        else:
            st.warning("Please provide a description of the attack.")

# Preemptive Analysis page
elif page == "Preemptive Analysis":
    st.title("Preemptive Analysis")
    st.write("Enter the details for preemptive analysis to identify and mitigate potential threats.")

    # Display sample prompts
    st.write("### Sample Prompts")
    selected_prompt = st.radio("Choose a sample prompt to use:", sample_prompts)

    if st.button("Use Sample Prompt", key="preemptive_sample"):
        st.session_state.analysis_description = selected_prompt

    # Use st.text_area with session_state to handle pre-filled text
    analysis_description = st.text_area(
        "Analysis Description",
        value=st.session_state.get('analysis_description', ''),
        placeholder="Describe the analysis scenario here..."
    )

    if st.button("Analyze"):
        if analysis_description.strip():  # Check if the text area is not empty
            analysis_result = deploy.mitigate(analysis_description)
            st.write("### Analysis Result")
            st.write(analysis_result)
        else:
            st.warning("Please provide a description for analysis.")

# Run the Streamlit app
if __name__ == "__main__":
    st.sidebar.write("Select a page to begin.")
