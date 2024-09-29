Fisk University Historical Chatbot Project
Project Overview
This project was initiated to create a reliable, easily accessible chatbot for students at Fisk University to reference when learning about the rich history and background of our college. Fisk University, founded in 1866, has an extensive and inspiring history that students often need to explore for various academic and personal reasons. Our chatbot project was built to fill this gap by providing an engaging and intelligent resource for students to retrieve historical facts, milestones, and notable events regarding Fisk University.

The core idea was to develop a tool that could deliver concise, accurate information, allowing students to quickly understand significant moments in Fisk’s legacy—anytime, anywhere.

The Chatbot Vision
The idea to create this chatbot was born out of a group discussion. We realized that, despite the historical significance of Fisk University, students often didn’t have a quick and reliable way to learn about its history. So, we decided to tackle the problem head-on by creating a solution that would act as an on-demand Fisk historian. Our chatbot would answer questions about Fisk’s history—important events, notable alumni, historical buildings, and the university's pivotal role in the Civil Rights Movement.

However, the journey was more challenging than we initially thought. Despite the excitement and passion fueling us, we ran into roadblocks during the process, particularly with the fine-tuning of models. But more on that later.

Project Structure and Key Technologies
We built the chatbot using a combination of technologies:

HTML, CSS, and JavaScript for the front-end: This formed the user interface for students to interact with the chatbot.
Python for back-end development: We used Flask to handle the API calls and the logic behind user queries.
Perplexity AI's API: Initially, we planned to scrape resources like Wikipedia to gather information and train a custom model. We built a dataset to feed into a Llama model. However, Perplexity AI did not support fine-tuning at the time. As a result, we relied on querying existing models.
Web scraping tools: We used scraping libraries to gather historical data from Wikipedia and other sources to build an informative dataset.
Vercel for hosting: The project was deployed on Vercel, ensuring high availability and scalability for our chatbot.
Development Journey: The All-Nighter
This project was a true labor of love, fueled by our passion for creating something impactful for the Fisk University community. Over the course of a single, sleepless night, our small but dedicated team of Computer Science majors came together. With several cans of Red Bull, a collective sense of vision, and sheer determination, we powered through obstacles—debugging code, testing our web app, and refining how the chatbot answered questions about Fisk's history.

Was it easy? Absolutely not. Did we sleep? Definitely not. But the shared excitement and passion for making something for our fellow students kept us going. And when you’re surrounded by passionate and visionary people who love to build things, it’s amazing what you can accomplish.

Teamwork and Commitment
As a team, we all played our part:

Backend Engineers took on the challenge of building Flask routes and managing the interactions between the user interface and the Perplexity API.
Frontend Developers designed the user experience, making sure the chatbot was not only functional but also aesthetically aligned with Fisk’s colors and theme.
Data Engineers scraped relevant historical information and built the dataset that would form the knowledge base of our chatbot.
Through late nights, troubleshooting sessions, and a unified sense of purpose, we pulled together to create something meaningful for our community.

Challenges and Technical Details
The Llama Model Hurdle
One of the major technical hurdles we faced was our inability to fine-tune the Llama model via Perplexity AI. Initially, we built a robust dataset scraped from Wikipedia, hoping to train a custom model to provide highly accurate and personalized answers specific to Fisk’s history. Unfortunately, Perplexity AI's platform did not allow us to fine-tune the model.

While this was a setback, we pivoted quickly. We adapted by using Perplexity AI’s default model for responses, and despite not having a fine-tuned model, the chatbot still delivered relevant, useful information. However, this has motivated us to look for future solutions to fine-tune models on other platforms, such as Hugging Face, for the next phase of the project.

Frontend and API Integration
On the frontend, we used HTML, CSS, and JavaScript to build a simple, intuitive interface. Students can type questions related to Fisk’s history, and the chatbot responds with information retrieved via API calls to Perplexity AI. Flask handles these requests on the backend, ensuring a smooth flow of data between the user's queries and the model's responses.

Hosting on Vercel
Our final chatbot was deployed on Vercel, providing easy hosting, deployment, and scalability. Vercel allowed us to make the project accessible to anyone with a web browser. Given its serverless architecture, Vercel was an excellent choice for hosting our chatbot while ensuring it remained fast and responsive under different loads.

Future Directions
This project is far from over! While the first iteration has been a success, we have several exciting plans for the future:

Fine-Tuning on Hugging Face: We plan to explore Hugging Face's model fine-tuning features. By fine-tuning models with our custom dataset on Fisk’s history, we hope to make the chatbot even more precise and capable of answering complex historical queries.

Expanding the Knowledge Base: Currently, the chatbot answers historical questions related to Fisk University, but we plan to expand its knowledge base to include faculty details, current events, and even information about academic programs.

Multilingual Support: Fisk University has a diverse student body. In the future, we’d love to extend the chatbot’s capabilities by incorporating multilingual support, making it accessible to even more students.

Mobile-Friendly Version: We want to ensure our project scales to mobile devices. As students increasingly rely on mobile devices, we aim to improve the user experience for mobile users, ensuring a smooth and accessible interface on the go.

Machine Learning Integration: As we grow more comfortable with machine learning, we plan to implement additional machine learning models that would provide personalized insights based on the type of historical information users ask for.

Conclusion
This chatbot project was more than just a technical challenge—it was a testament to what can be achieved with passion, teamwork, and a vision. We came together as visionary CS majors who are deeply committed to building tools that serve our school community. With a few cans of Red Bull, some determination, and the belief that anything is possible, we turned an idea into reality.

Stay tuned for the next iteration—this is only the beginning!
