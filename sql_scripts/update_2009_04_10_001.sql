﻿ALTER TABLE Tag ADD COLUMN deleted_at datetime default null;
ALTER TABLE Tag ADD COLUMN deleted_by_id INTEGER NULL;
ALTER TABLE Tag ADD COLUMN deleted TINYINT NOT NULL;
