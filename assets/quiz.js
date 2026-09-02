/* Reusable retrieval-practice quiz widget for the Bike Frame Craft course.
   A lesson declares quizzes as JSON in a <script type="application/json"
   class="quiz-data"> block inside a .quiz container:

   { "question": "...",
     "options": ["A", "B", "C", "D"],
     "answer": 1,
     "explain": "Shown after any click." }

   Feedback is immediate — click an option, see right/wrong plus the
   explanation. Wrong answers stay clickable so the learner can retrieve
   again rather than being told the answer. */

(function () {
  function renderQuiz(container, data, index) {
    var title = document.createElement('h3');
    title.textContent = 'Check yourself · ' + index;
    container.appendChild(title);

    var q = document.createElement('p');
    q.className = 'q-text';
    q.textContent = data.question;
    container.appendChild(q);

    var feedback = document.createElement('p');
    feedback.className = 'q-feedback';

    data.options.forEach(function (opt, i) {
      var btn = document.createElement('button');
      btn.className = 'q-opt';
      btn.type = 'button';
      btn.textContent = opt;
      btn.addEventListener('click', function () {
        if (i === data.answer) {
          btn.classList.add('correct');
          feedback.className = 'q-feedback good';
          feedback.textContent = '✓ Right. ' + (data.explain || '');
          container.querySelectorAll('.q-opt').forEach(function (b) {
            b.disabled = true;
            if (b !== btn) b.classList.remove('wrong');
          });
        } else {
          btn.classList.add('wrong');
          btn.disabled = true;
          feedback.className = 'q-feedback bad';
          feedback.textContent = '✗ Not that one. Try again from memory.';
        }
        if (!feedback.parentNode) container.appendChild(feedback);
      });
      container.appendChild(btn);
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.quiz').forEach(function (container, idx) {
      var dataEl = container.querySelector('.quiz-data');
      if (!dataEl) return;
      try {
        renderQuiz(container, JSON.parse(dataEl.textContent), idx + 1);
      } catch (e) {
        container.textContent = 'Quiz failed to load.';
      }
    });
  });
})();
