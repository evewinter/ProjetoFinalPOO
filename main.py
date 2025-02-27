from Cantor import Cantor, Solista, Grupo
from Gravadora import Gravadora, Subsidiaria

Sony = Gravadora("Sony Music", "USA")
Warner = Gravadora("Warner Music", "USA")
Universal = Gravadora("Universal Music", "Reino Unido")
Columbia = Subsidiaria("Columbia Records", "USA", "Sony")
Atlantic = Subsidiaria("Atlantic Records", "USA", "Warner")

Normani = Solista("Normani", "Norte Americada", Sony, 8000.00, "Pop")
BrunoMars = Solista("Bruno Mars", "Norte Americano", Warner, 9500.00, "Pop")
BillieEilish = Solista("Billie Eilish", "Norte Americana", Universal, 10956.00, "Pop")
ChappellRoan = Solista("ChappelRoan", "Norte Americana", Atlantic, 7865.00, "Pop")
DoveCameron = Solista("Dove Cameron", "Norte Americana", Columbia, 6400.26, "Pop")

Tilibra = Grupo("Tilibra", "Australia", Columbia, "Tilibra", 20600.00)

Tilibra.adicionar_membro(Normani)
Tilibra.adicionar_membro(BrunoMars)
Tilibra.adicionar_membro(BillieEilish)

Sony.contratar_artista(Normani)
Warner.contratar_artista(BrunoMars)
Universal.contratar_artista(BillieEilish)
Columbia.contratar_artista(DoveCameron)
Columbia.contratar_artista(Tilibra)
Atlantic.contratar_artista(ChappellRoan)

for gravadora in [Sony, Warner, Universal, Columbia, Atlantic]:
    print(f"\nArtistas da {gravadora.nome}:")
    for cantor in gravadora.totaldecantores:
        if isinstance(cantor, Grupo):
            print(f" {cantor.nome_do_grupo} (Grupo). Membros: {" , ".join(m.nome for m in cantor.membros)}.")
        else:
            print(f" {cantor.nome}, Estilo: {getattr(cantor, 'estilo_musical', 'N/A')}")

print("\nGravadoras: ")
for gravadora in [Sony, Warner, Universal]:
    print(f"Nome: {gravadora.nome}, País: {gravadora.pais}")

print("\nSubsidiárias: ")
print(f"Nome: {Columbia.nome}, País: {Columbia.pais}, Selo: {Columbia.selo}")
print(f"Nome: {Atlantic.nome}, País: {Atlantic.pais}, Selo: {Atlantic.selo}\n")

print(BrunoMars.apresentar())

print(Tilibra.apresentar())
