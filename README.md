# YouTube Comment Analysis

Этот проект анализирует комментарии с видео на YouTube и выделяет темы с использованием модели Latent Dirichlet Allocation (LDA).

## Структура проекта

```
comment_analysis/
├── data/
│ ├── raw/
│ │ └── comments_raw.json
│ └── processed/
│ └── comments_preprocessed.json
├── models/
│ └── lda_model.pkl
├── notebooks/
│ └── exploratory_data_analysis.ipynb
├── scripts/
│ ├── data_collection.py
│ ├── preprocessing.py
│ └── topic_modeling.py
├── utils/
│ ├── youtube_api.py
│ └── text_processing.py
├── requirements.txt
└── README.md #
```

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/youtube_comments_analysis.git
   cd comment_analysis
2. Создайте и активируйте виртуальное окружение:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

## Использование

1. Сбор данных:
Извлеките комментарии с YouTube видео, запустив следующий скрипт:
  ```
  python scripts/data_collection.py
  ```
Убедитесь, что вы добавили ваш YouTube API ключ и идентификатор видео в файл data_collection.py.

2. Предобработка данных:
Очистите и подготовьте данные для анализа:

  ```
  python scripts/preprocessing.py
  ```

3. Обучение модели и выделение тем:
Обучите модель LDA и выделите основные темы из комментариев:
  ```
  python scripts/topic_modeling.py
  ```

## Описание файлов

- `data/raw/comments_raw.json`: Сырые данные комментариев, извлеченные с YouTube.
- `data/processed/comments_preprocessed.json`: Предобработанные данные комментариев, очищенные от ненужных символов и ссылок.
- `models/lda_model.pkl`: Сохраненная модель LDA для тематического анализа.
- `notebooks/exploratory_data_analysis.ipynb`: Jupyter Notebook для разведочного анализа данных.
- `scripts/data_collection.py`: Скрипт для сбора данных из YouTube.
- `scripts/preprocessing.py`: Скрипт для предобработки текста комментариев.
- `scripts/topic_modeling.py`: Скрипт для обучения модели LDA и выделения тем.
- `utils/youtube_api.py`: Вспомогательные функции для работы с YouTube API.
- `utils/text_processing.py`: Вспомогательные функции для предобработки текста.

## Примечания

- Вам понадобится API ключ YouTube для извлечения комментариев. Создайте проект в Google Developer Console, активируйте YouTube Data API v3 и создайте API ключ.
- Этот проект использует LDA для тематического анализа, но вы можете попробовать другие методы, такие как NMF, для улучшения результатов.

## Автор

Пешков Матвей (https://github.com/Peshkov-Matvei).
