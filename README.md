# README.md

## Summary

Carousel aims to revolutionize user interfaces using the intelligence of Large Language Models to generate custom HTML5 pages as needed.

## Quick Start

1. Create a local environment variable called `OPENAI_API_KEY` and place your OpenAI API key in it.
1. Install requirements (a virtual environment is recommended but not required):

> python -m pip install -r requirements.txt

1. Start Flask:

> python run.py

1. Navigate to the webapp in your browser:

> http://localhost:5000

1. To close the application, press CTRL-C in the console window (for most consoles)

## Revolutionizing User Interfaces: An AI-driven Approach Leveraging HTML-response Interpretation

### The AI-Driven UI Proposal

Our project envisions a shift towards a highly effective AI chatbot as a UI mediator. By employing advanced AI technologies like the Whisper voice system, we aim to empower users to interact with a system via voice or text commands. The AI parses the instructions, accesses the required data, and generates the desired results.

The transformative shift here is the AI's ability to respond with HTML, creating an interactive experience. Instead of buttons triggering back-end processes, they inform the AI of the user interaction. This interaction could be a button press, dial settings, or text input. The AI interprets this, decides on the expected behavior, and responds with an updated HTML page or components.

### Potential Benefits

1. **Personalized Interface**: As the AI learns the user's preferences, it can personalize the interface in real time to meet individual needs.
2. **Adaptability**: The interface can adapt to the task at hand, offering a more streamlined and task-focused UI.
3. **Accessibility**: Voice interaction could make technology more accessible to those with limited digital skills or physical impairments.
4. **Efficiency**: With the AI handling user input interpretation and backend function triggering, developers can focus on enhancing the AI's capabilities rather than updating the UI.

### Impact on App Development 

The introduction of AI-mediated interfaces promises to significantly transform the application development landscape. By offloading the task of user-input interpretation and response generation to the AI, the development process could become more straightforward, cost-effective, and expedited.

- **Simplified Design & Development**: The focus shifts from designing static UI elements to developing the AI's ability to generate dynamic, user-oriented HTML responses.
- **Efficient Handling of Edge Cases**: The AI uses its general knowledge, Theory of Mind, and other insights to interpret and respond to user inputs appropriately, including handling unexpected user requests.
- **Cost and Time Efficiency**: By reducing the complexity involved in UI design and edge case handling, we anticipate a significant reduction in development time and cost.
- **Focus on Enhancing AI**: Developers can focus on enhancing the AI's capabilities, training it to better understand user instructions, preferences, and needs.

### Cognitive Architecture

In order to fully leverage the AI for interface generation, the AI must have the ability to both store and reference relevant data. This data may have various purposes, such as data relevant to the UI creation process itself, data required as content, or memory of past events. It may also be necessary to leverage different AI models for their respective strengths, such as a chat model for interfacing directly with the user, and coding models for generating html, css, and javascript.

Each of these components will be integrated modularly in order to make them easily replaced by more advanced versions.

Definitions of Information Modules:

1. Semantic Memory: Search of a database of factual information.
2. Episodic Memory: Search of events in time, such as past conversations.
3. Web Search: Search of the web.
4. Carousel: Search of a database of past pages which were flagged for storage by the user.

![Carousel Cognitive Architecture](./assets/Carousel%20Cognitive%20Architecture%20Diagram.svg)

### Minimum Viable Product (MVP)

MVP Requirements:

1. User can interact with a chatbot.
2. All chatbot responses either generate a web page or update its files or elements.
3. A static UI component exists for interacting with the chatbot even in the case of a page display failure so that the user can request a new page.

Initially, Carousel will be the only Information Module provided. The rest, while valuable enhancements, are not required for the minimum viable product

### Conclusion

Transitioning towards an AI-driven UI model could be a game-changer in app use and development, making it more streamlined, cost-effective, and efficient. This approach maximizes the potential of AI and paves the way for a new generation of apps that are smarter, more personalized, and more intuitive to use.

Join us as we embark on this exciting journey to revolutionize user interfaces. Your contributions, ideas, and feedback are most welcome!

## Unit Tests

> export PYTHONPATH=$PYTHONPATH:/path/to/your/project/root
> python -m unittest discover tests