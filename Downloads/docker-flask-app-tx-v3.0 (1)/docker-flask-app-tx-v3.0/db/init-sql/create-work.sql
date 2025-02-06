-- テーブル作成
CREATE TABLE Work (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    created TEXT NOT NULL ,
    hourly_wage TEXT NOT NULL,
    people TEXT NOT NULL
);

-- ダミーデータ挿入
INSERT INTO Work (id, title, content, created, hourly_wage, people) VALUES
('3b4b60c6-3a90-48c9-b8ed-4df5d1231231', '杉並区セブンイレブン 品出し', '未経験大歓迎 簡単な品出しです！', '2025年01月03日 22:00 ~ ４時間 ', '1300円', '2人'),
('4a2b8e87-2c34-490e-80f7-123b456c7892', '倉庫 仕分け作業', '日払いOK モクモク作業が向いてる人おすすめ', '2025年01月03日 19:00 ~ 23:00 ４時間', '1500円', '5人'),
('d5f3ac91-9f64-4b82-b27a-c7d1b3cd5672', '高円寺徒歩１分 吉野家 洗い場 or ホールバイト', '賄いあり 人気なため、お早めに', '2025年01月03日 11:00~ 14:00 3時間', '1220円','3人');



