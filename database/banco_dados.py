from datetime import date, datetime
from sqlalchemy import create_engine, select, String, Integer, Boolean, Date, DateTime, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

engine = create_engine('sqlite:///dados.db')
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass


class Usuario(Base):
    __tablename__ = 'usuario'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    admin: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    cpf: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    data_nascimento: Mapped[date] = mapped_column(Date, nullable=False)
    login: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(String, nullable=False)
    pontos: Mapped[int] = mapped_column(Integer, nullable=False, default=100)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    data_cadastro: Mapped[date] = mapped_column(Date, nullable=False, default=date.today)



class Aposta(Base):
    __tablename__ = 'aposta'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    idUsuario: Mapped[int] = mapped_column(Integer, ForeignKey('usuario.id'), nullable=False)
    idJogo: Mapped[int] = mapped_column(Integer, ForeignKey('jogo.id'), nullable=False)
    data_aposta: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    valor_aposta: Mapped[int] = mapped_column(Integer, nullable=False)
    multiplicar_aposta: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)



class Jogo(Base):
    __tablename__= 'jogo'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    time_casa: Mapped[str] = mapped_column(String, nullable=False)
    time_fora: Mapped[str] = mapped_column(String, nullable=False)
    resultado: Mapped[int] = mapped_column(Integer, nullable=False)
    odd: Mapped[float] = mapped_column(Float, nullable=False)


def inserir_usuario(usuario):
    with Session() as session:
        session.add(usuario)
        session.commit()




def buscar_usuario_por_login(login:str):
    with Session() as session:
        stmt = select(Usuario).where(Usuario.login == login)
        usuario = session.scalars(stmt).first()
        return usuario



def inserir_aposta(aposta):
    with Session() as session:
        session.add(aposta)
        session.commit()


def atualizar_pontos(usuario_id: int, novos_pontos: int):
    with Session() as session:
        usuario = session.get(Usuario, usuario_id)
        if usuario:
            usuario.pontos = novos_pontos
            session.commit()












Base.metadata.create_all(engine)