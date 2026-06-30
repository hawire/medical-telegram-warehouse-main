SELECT

    d.message_id,

    f.channel_key,

    f.date_key,

    d.detected_class,

    d.confidence_score,

    d.image_category

FROM {{ ref('fct_messages') }} f

JOIN raw.image_detections d

ON f.message_id = d.message_id
