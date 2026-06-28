
SELECT
    message_id,
    message_text,
    views,
    forwards,
    LENGTH(message_text) AS message_length
FROM telegram_messages
