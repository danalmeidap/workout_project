from workout_project.repositories.atleta import (
    atualizar_atleta,
    criar_atleta,
    deletar_atleta,
    listar_atletas,
    obter_atleta_por_id,
)
from workout_project.schemas.atleta import AtletaIn, AtletaUpdate


def test_criar_atleta(db):
    atleta_in = AtletaIn(
        nome="Teste Atleta",
        cpf="12345678901",
        idade=30,
        peso=80.0,
        altura=1.80,
        sexo="M",
        categoria_id=1,  # Estes IDs devem existir ou ser mockados
        centro_treinamento_id=1,
    )
    atleta = criar_atleta(db, atleta_in)
    assert atleta.pk_id is not None
    assert atleta.nome == "Teste Atleta"


def test_obter_atleta_por_id(db):
    atleta_in = AtletaIn(
        nome="Busca ID",
        cpf="99988877766",
        idade=30,
        peso=80.0,
        altura=1.80,
        sexo="M",
        categoria_id=1,
        centro_treinamento_id=1,
    )
    novo_atleta = criar_atleta(db, atleta_in)

    atleta_encontrado = obter_atleta_por_id(db, novo_atleta.pk_id)
    assert atleta_encontrado is not None
    assert atleta_encontrado.nome == "Busca ID"


def test_listar_atletas(db):
    atleta_in1 = AtletaIn(
        nome="Atleta 1",
        cpf="11122233344",
        idade=25,
        peso=70.0,
        altura=1.70,
        sexo="M",
        categoria_id=1,
        centro_treinamento_id=1,
    )
    atleta_in2 = AtletaIn(
        nome="Atleta 2",
        cpf="55566677788",
        idade=28,
        peso=75.0,
        altura=1.75,
        sexo="M",
        categoria_id=1,
        centro_treinamento_id=1,
    )
    criar_atleta(db, atleta_in1)
    criar_atleta(db, atleta_in2)

    atletas = listar_atletas(db)
    RESPOSTA_CORRETA = 2
    assert len(atletas) == RESPOSTA_CORRETA


def test_deletar_atleta_sucesso(db):
    atleta_in = AtletaIn(
        nome="Deletar",
        cpf="55544433322",
        idade=25,
        peso=65.0,
        altura=1.65,
        sexo="F",
        categoria_id=1,
        centro_treinamento_id=1,
    )
    novo_atleta = criar_atleta(db, atleta_in)

    resultado = deletar_atleta(db, novo_atleta.pk_id)
    assert resultado is True

    atleta_deletado = obter_atleta_por_id(db, novo_atleta.pk_id)
    assert atleta_deletado is None


def test_deletar_atleta_nao_existente(db):
    resultado = deletar_atleta(db, 99999)
    assert resultado is False


def test_atualizar_atleta_sucesso(db):
    atleta_in = AtletaIn(
        nome="Original",
        cpf="11111111111",
        idade=30,
        peso=80.0,
        altura=1.80,
        sexo="M",
        categoria_id=1,
        centro_treinamento_id=1,
    )
    novo_atleta = criar_atleta(db, atleta_in)
    atleta_update = AtletaUpdate(
        nome="Atualizado",
        peso=85.0,
    )

    atleta_atualizado = atualizar_atleta(db, novo_atleta.pk_id, atleta_update)
    PESO = 85.0
    assert atleta_atualizado is not None
    assert atleta_atualizado.nome == "Atualizado"
    assert atleta_atualizado.peso == PESO
    assert atleta_atualizado.cpf == "11111111111"  # CPF não deve ser alterado


def test_atualizar_atleta_nao_existente(db):
    atleta_update = AtletaUpdate(nome="Não Existe")
    atleta_atualizado = atualizar_atleta(db, 99999, atleta_update)
    assert atleta_atualizado is None
