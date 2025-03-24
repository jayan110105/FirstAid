function checkQuiz(quizId, correctAnswers) {
    let quiz = document.getElementById(quizId);
    let answers = quiz.querySelectorAll("input[type=radio]:checked");
    let feedback = document.getElementById(quizId + "Feedback");
    let score = 0;

    answers.forEach((answer, index) => {
        if (answer.value === correctAnswers[index]) {
            score++;
        }
    });

    feedback.textContent = `You got ${score} out of ${correctAnswers.length} correct!`;
}
