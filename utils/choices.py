# 塾の授業日
# 左側はintが推奨？(Shift複製時に使用)
DAY_CHOICES = [
    (1, '月曜日'),
    (2, '火曜日'),
    (3, '水曜日'),
    (4, '木曜日'),
    (5, '金曜日'),
]

# 塾の授業時間
# 16:30-17:30の形式で設定
TIME_CHOICES = [
    (1, '16:30-17:30'),
    (2, '17:35-18:35'),
    (3, '18:40-19:40'),
    (4, '19:50-20:50'),
    (5, '21:00-22:00'),
]

# 講習授業の特別授業
SPECIAL_TIME_CHOICES = [
    (6, '14:10-15:10'),
    (7, '15:20-16:20'),
]

# 塾の授業科目
SUBJECT_CHOICES = [
    (1, '国語'),
    (2, '数学'),
    (3, '英語'),
    (4, '社会'),
    (5, '理科'),
]

# 塾の教室選択
ROOM_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
]

# 学年の選択
GRADE_CHOICES = [
    (1, '小1'),
    (2, '小2'),
    (3, '小3'),
    (4, '小4'),
    (5, '小5'),
    (6, '小6'),
    (7, '中1'),
    (8, '中2'),
    (9, '中3'),
    (10, '高1'),
    (11, '高2'),
    (12, '高3'),
    (13, '高3以降'),
]

GRADE_MIDDLE_CHOICES = [
    (7, '中1'),
    (8, '中2'),
    (9, '中3'),
]

# 学校の選択
SCHOOL_CHOICES = [
    (1, '中部'),
    (2, '別府'),
    (3, '浜の宮'),
    (4, '加古川'),
    (5, '神吉'),
    (6, '氷丘'),
]

# 給与の種類(0は普段は使用しない)
SALARY_CHOICES = [
    (0, '授業手当'),
    (1, '事務手当'),
    (2, '通勤手当'),
    (3, '研修手当'),
]
