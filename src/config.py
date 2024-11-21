class Config:
    # "Константы" с начальными значениями
    NUMBER_PLAYERS = 3
    NAME_PLAYERS = []

    def update_number_players(value):
        """Обновить количество игроков."""
        Config.NUMBER_PLAYERS = value

    def update_name_players(names):
        """Обновить список имен игроков."""
        Config.NAME_PLAYERS = names.copy()