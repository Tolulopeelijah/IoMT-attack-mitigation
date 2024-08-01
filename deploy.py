import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('openai_key')


def generate(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=200,
        temperature=0.7,
        top_p=1.0,
    )

    return response.choices[0].message['content'].strip()




def mitigate(description):
    prompt = \
        f'''Generate a step by step mitigation solution and the type of attack in the following description 
    {description}
    Mitigation steps:

    '''
    return generate(prompt)


def simulate(attack_type):
    prompt = \
        f'''Generate a possible, relevant, creative, practical scenario of {attack_type} attack in IoMT devices used in healthcare
    A possible scenario:
    '''
    return generate(prompt)

# print(mitigate("My insulin pump has been working fine, but lately, I've noticed Traffic was observed with the following characteristics: Header length of 36043.6 bytes, using the 6.0 protocol. The connection duration was 64.0 seconds with a rate of 1.3366900608925942 bytes per second, and source rate 1.3366900608925942 bytes per second. The packet contains 0.0 SYN flags, 0.0 RST flags, and 1.0 ACK flags. The SYN packet count is 0.0, FIN packet count is 0.0, and RST packet count is 466.5. TCP traffic is present (1.0), UDP traffic is present (0.0), ICMP traffic is present (0.0), IPv traffic is present (1.0), and LLC traffic is present (1.0). Statistical measures include a total sum of 413.7, minimum value of 66.0, maximum value of 85.8, average of 74.4020238095238, standard deviation of 9.176143913768222, total size of 76.3 bytes, inter-arrival time of 7.359981536865234e-05 microseconds, number of packets 5.5, magnitude 12.1959306758997, radius 12.97702717313835, covariance 93.66396697845803, variance 0.9, and weight 38.5.. I'm not sure if it's just a glitch, but it's making me anxious. What should I do?"))