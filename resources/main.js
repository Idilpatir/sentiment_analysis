window.count.addEventListener('input', e => {
	window.count_value.textContent = `${e.target.value}/${e.target.max}`
});

function OpenHandler(e) {
	const target = e.target.closest('.comment').getAttribute('href');
	window.open(target, '_blank');
}

function CreateCommentElement(comment) {
	const commentContainerElement = document.createElement('div');
	commentContainerElement.classList.add('comment');
	commentContainerElement.setAttribute('href', comment.href);

	const commentHeaderElement = document.createElement('div');
	commentHeaderElement.classList.add('comment-header');

	const leftSideHeaderElement = document.createElement('h2');

	const icon = document.createElement('i');
	icon.classList.add('fa-solid', 'fa-arrow-up-right-from-square', 'open-external-icon');
	icon.addEventListener('click', OpenHandler);
	leftSideHeaderElement.appendChild(icon);

	const userNameElement = document.createElement('span');
	userNameElement.textContent = comment.userName;
	leftSideHeaderElement.appendChild(userNameElement);

	const rightSideHeaderElement = document.createElement('h2');
	rightSideHeaderElement.textContent = `${comment.score} - ${comment.emotion}`;

	commentHeaderElement.appendChild(leftSideHeaderElement);
	commentHeaderElement.appendChild(rightSideHeaderElement);
	commentContainerElement.appendChild(commentHeaderElement);

	const commentBodyElement = document.createElement('p');
	commentBodyElement.textContent = comment.comment;
	commentContainerElement.appendChild(commentBodyElement);

	window.comment_container.appendChild(commentContainerElement);
}

function LoadComments(comments) {
	window.comment_container.innerHTML = '';

	for (let i = 0; i < comments.length; i++) {
		CreateCommentElement(comments[i]);
	}
}
function LoadCharts(comments) {
	const scores = Object.create(null);
	const emotions = Object.create(null);

	for (let i = 0; i < comments.length; i++) {
		let comment = comments[i];
		emotions[comment.emotion] = (emotions[comment.emotion] || 0) + 1;
		const scoreRange = Math.floor(comment.score);
		scores[scoreRange] = (scores[scoreRange] || 0) + 1; 
	}

	new Chart(
		window.sentiment_canvas.getContext('2d'),
		{
			type: 'pie',
			data: {
				labels: ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10'],
				datasets: [{
					label: '# of Comments',
					data: [scores[0], scores[1], scores[2], scores[3], scores[4], scores[5], scores[6], scores[7], scores[8], scores[9]],
					borderWidth: 1
				}]
			}
		}
	)

	new Chart(
		window.emotion_canvas.getContext('2d'),
		{
			type: 'pie',
			data: {
				labels: Object.keys(emotions),
				datasets: [{
					label: '# of Comments',
					data: Object.values(emotions),
					borderWidth: 1
				}]
			}
		}
	)
}

function LoadData(videoName, videoImage, comments) {
	window.video_name.textContent = videoName;

	const averageScore = comments.reduce((a, b) => a + b.score, 0) / comments.length;
	window.average_score.textContent = `Average Score: ${averageScore}`

	window.video_image.src = videoImage;
}

const comments = [];

const testEmotions = ['Angry', 'Joyful', 'Surprised', 'Disgusted', 'Fearful', 'Satisfied', 'Bored', 'Happy', 'Neutral', 'Sad'];

for (let i = 0; i < 20; i++) {
	comments.push({
		href: 'https://google.com',
		userName: 'İdil ' + i,
		score: i%10,
		emotion: testEmotions[i%testEmotions.length],
		comment: 'This is a comment'
	});
}

LoadComments(comments);
LoadCharts(comments);
LoadData('İdilin süper videosu', 'resources/7.png', comments);

console.log(comments);