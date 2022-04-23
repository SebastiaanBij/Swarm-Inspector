#!/usr/bin/env python3

# ||Imports||
# -------------------------------------------------------------------------------------------------------------------- #
from datetime import datetime

# ||Classes||
# -------------------------------------------------------------------------------------------------------------------- #
class PIDsStats:
    # region Constructor
    def __init__(self, current: int):
        self.__current = current
    # endregion

    # region Properties
    @property
    def current(self) -> int:
        return self.__current
    # endregion

class ContainerStats:
    # region Constructor
    def __init__(self, read: str, preread: str, pids_stats: PIDsStats):
        self.__read_date = datetime.strptime(read, "%Y-%m-%dT%H:%M:%S.%fZ")
        self.__pre_read_date = datetime.strptime(preread, "%Y-%m-%dT%H:%M:%S.%fZ")
        self.__pids_stats = pids_stats
    # endregion

    # region Properties
    @property
    def read_data(self) -> datetime:
        return self.__read_date

    @property
    def pre_read_data(self) -> datetime:
        return self.__pre_read_date

    @property
    def pids_stats(self) -> PIDsStats:
        return self.__pids_stats
    # endregion
