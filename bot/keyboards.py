from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




back_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(callback_data="Назад", text="Назад", )
        ]
    ]
)


levels_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Бакалавриат', callback_data='Бакалавриат')],
        [InlineKeyboardButton(text='Магистратура', callback_data='Магистратура')],
        [
        InlineKeyboardButton(text='Аспирантура', callback_data='Аспирантура'),
        ]
    ]
)

directions_bakalavr = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Социальная работа', callback_data='bac_soc_work')
        ],
        [
            InlineKeyboardButton(text='Организация работы с молодежью', callback_data='bac_org_work'),
        ],
        [
            InlineKeyboardButton(text='Журналистика', callback_data='bac_journalist')
        ],
        [
            InlineKeyboardButton(text='Гостиничное дело', callback_data='bac_hostel')
        ],
        [
            InlineKeyboardButton(text='Педагогическое образование', callback_data='bac_ped')
        ],
        [
            InlineKeyboardButton(text='Специальное (дефектологическое) образование', callback_data='bac_spec')
        ],
        [
            InlineKeyboardButton(text='Документоведение и архивоведение', callback_data='bac_docs')
        ],
                [
            InlineKeyboardButton(text='физическая культура', callback_data='bac_fk')
        ],
        [
            InlineKeyboardButton(text='адаптивная физическая культура', callback_data='bac_afk')
        ],
        [
          InlineKeyboardButton(text='Социально-культурная деятельность', callback_data='bac_soc_culture')
        ],
        [
            InlineKeyboardButton(text='Дизайн', callback_data='bac_design')
        ],
                [
        InlineKeyboardButton(callback_data="Назад", text="Назад", )
        ]
        

    ]
)

directions_magistr = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Психология', callback_data='mag_psycho')
        ],
                [
            InlineKeyboardButton(text='Социология', callback_data='mag_soc')
        ],
                [
            InlineKeyboardButton(text='Социальная работа', callback_data='mag_soc_work')
        ],
                [
            InlineKeyboardButton(text='Педагогическое образование', callback_data='mag_ped')
        ],
                [
            InlineKeyboardButton(text='Специальное образование', callback_data='mag_spec')
        ],
                [
            InlineKeyboardButton(text='Документоведение и архивоведение', callback_data='mag_docs')
        ],
                [
            InlineKeyboardButton(text='Антропология и этнология', callback_data='mag_antrop')
        ],
                [
            InlineKeyboardButton(text='Спорт', callback_data='mag_sport')
        ],
                [
        InlineKeyboardButton(callback_data="Назад", text="Назад", )
        ]

    ]
)
directions_aspir = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Физиология человека и животных', callback_data='aspir_fiz')
        ],
        [
            InlineKeyboardButton(text='Педагогическая психология, психодиагностика цифровых образовательных сред', callback_data='aspir_ped_psycho'),
        ],
                [
            InlineKeyboardButton(text='Социальная структура, социальные институты и процессы', callback_data='aspir_cos')
        ],
        [
            InlineKeyboardButton(text='Отечественная история', callback_data='aspir_history'),
        ],
                [
            InlineKeyboardButton(text='Общая педагогика, история педагогики и образования', callback_data='aspir_ped')
        ],
        [
            InlineKeyboardButton(text='Коррекционная педагогика ', callback_data='aspir_kor_ped'),
        ],
        [
            InlineKeyboardButton(text='Физическая культура и профессиональная физическая подготовка', callback_data='aspir_fk')
        ],
        [
            InlineKeyboardButton(text='Теория и методика спорта', callback_data='aspir_sport'),
        ],
        [
            InlineKeyboardButton(text='Оздоровительная и адаптивная физическая культура', callback_data='aspir_adapt_fk'),
        ],
        [
            InlineKeyboardButton(text='Методология и технология профессионального образования', callback_data='aspir_prof_edu'),
        ],
        [
            InlineKeyboardButton(text='Русская литература и литературы народов Российской Федерации', callback_data='aspir_literature'),
        ],
        [
            InlineKeyboardButton(text='Русский язык. Языки народов России', callback_data='aspir_russian'),
        ],      
        [
            InlineKeyboardButton(text='Теоретическая, прикладная и сравнительно-сопоставительная лингвистика', callback_data='aspir_lingv'),
        ],
        [
        InlineKeyboardButton(callback_data="Назад", text="Назад", )
        ]
    ]
)