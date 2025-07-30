from injector import Module, provider, singleton
from account.infrastructure.database.repository.mapper import AccountMapper
from account.infrastructure.database.repository.rdb import AccountRepository
from account.application.service import AccountService


class AccountContainer(Module):
    @provider
    @singleton
    def provide_mapper(self) -> AccountMapper:
        return AccountMapper()

    @provider
    @singleton
    def provide_repository(self, mapper: AccountMapper) -> AccountRepository:
        return AccountRepository(mapper)

    @provider
    @singleton
    def provide_service(self, repository: AccountRepository) -> AccountService:
        return AccountService(repository)
