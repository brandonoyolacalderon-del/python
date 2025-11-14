#PROGRAMA QUE GENERA FACTURAS 
#REALIZADO POR BRANDON OYOLA CALDERON Y SANTIAGO CAICEDO SERRATO
IVA_PORCENTAJE = 0.19 
total_bruto = 0.0
detalles_factura = []
continuar = 'S'

print("--- SISTEMA GENERADOR DE FACTURAS ---")

while continuar == 'S':
    print("\n--- Añadir Producto ---")
    
    nombre = input("Nombre del producto: ")
    
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            precio_unitario = float(input("Precio unitario ($): "))
            
            if cantidad <= 0 or precio_unitario <= 0:
                print("La cantidad y el precio deben ser mayores a cero.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese números válidos.")

    subtotal = cantidad * precio_unitario
    detalles_factura.append((nombre, cantidad, precio_unitario, subtotal))
    total_bruto += subtotal
    
    # Preguntar si desea añadir otro producto
    continuar = input("¿Desea añadir otro producto? (S/N): ").upper()
    if continuar != 'S':
        break

valor_iva = total_bruto * IVA_PORCENTAJE
total_neto = total_bruto + valor_iva

print("\n" + "="*50)
print(f"{'F A C T U R A':^50}")
print("="*50)

print(f"{'Producto':<20}{'Cant.':>8}{'P. Unit':>10}{'Subtotal':>12}")
print("-" * 50)

for nombre, cant, precio, subtotal in detalles_factura:
    print(f"{nombre:<20}{cant:>8}{precio:>10.2f}{subtotal:>12.2f}")

print("-" * 50)
print(f"{'Total Bruto:':<38}{total_bruto:>10.2f}")
print(f"{f'IVA ({int(IVA_PORCENTAJE*100)}%):':<38}{valor_iva:>10.2f}")

print("=" * 50)
print(f"{'TOTAL DE LA VENTA:':<38}{total_neto:>10.2f}")
print("=" * 50)

if total_neto > 500.00:
    print("¡Gracias por su compra grande! Vuelva pronto.")
else:
    print("¡Gracias por su compra!")


