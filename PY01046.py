
def thap_ha_noi(so_dia, cot_nguon, cot_trung_gian, cot_dich):
    if so_dia == 1:
        print(f"{cot_nguon} -> {cot_dich}")
        return
    thap_ha_noi(so_dia - 1, cot_nguon, cot_dich , cot_trung_gian)

    print(f"{cot_nguon} -> {cot_dich}")

    thap_ha_noi(so_dia - 1, cot_trung_gian, cot_nguon,  cot_dich)


so_dia = int(input())

if 0 < so_dia < 10:
    thap_ha_noi(so_dia, 'A', 'B', 'C')