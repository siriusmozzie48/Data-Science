Quizzes are a useful way to practice what you or your students have learned and to keep track of progress. In this project, you'll build a educational quiz bot to help you generate quiz questions. Imagine you are a teacher needing to create a pop quiz based on your most recent lecture, or you are a student wanting to quiz yourself on this lecture. This tool will help you automate this task, track which questions have been asked to avoid repetition, and validate the responses.

You'll leverage OpenAI and prompt engineering to generate relevant questions.

The Data:
This quiz bot allows you to generate quizzes from any educational text. You have been provided with a sample data file from a physics-focused corpus, stored in the physics_lecture.txt file.

The text covers fundamental physics concepts, including speed, velocity, Newton's third law, and more. This content is sourced from ScienceQA (Saikh et al., 2022), a dataset originally designed for Machine Reading Comprehension (MRC) tasks. For this project, the dataset has been filtered to focus specifically on natural science topics related to physics, making it ideal for use with the quiz bot.

Source: https://huggingface.co/datasets/tasksource/ScienceQA_text_only?row=40 Saikh, Tanik et al. “ScienceQA: a novel resource for question answering on scholarly articles.” International Journal on Digital Libraries 23 (2022): 289 - 301.