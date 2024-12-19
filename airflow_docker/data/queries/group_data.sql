SELECT
    a.userID,
    a.surveyID,
    a.answerText,
    q.questionText,
    q.questionID
FROM answer a
INNER JOIN question q ON a.questionID = q.questionID
INNER JOIN survey s ON a.surveyID = s.surveyID
ORDER BY a.userID;
