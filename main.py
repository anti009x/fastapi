
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

from enum  import Enum

aplication = FastAPI()

transaksi_detaill = [  ]

transaksiii = ["BRI" , "BNI" , "SEA" , "DANA" ,"DANA"]

class tipe (str,Enum):
    def __str__(self):
        return str(self.value)
    PEMBELIAN = "PEMBELIAN"
    PENGEMBALIAN = "PENGEMBALIAN"
    
class pembayaran (str,Enum):
    def __str__(self):
        return str(pembayaran.value)
    BANK = transaksiii,
    [print(x) for x in BANK]
    print (len(BANK))

    

    
    
class InputTransaksi(BaseModel):
    tipe:tipe
    produk:str
    harga:int
    notes:Optional[str]
    pembayaran:pembayaran
    
    
#batasan transaksi

@aplication.get("/transaksi")
def get_transaksi(prodak: str, harga: int):
    try:
        hargaparsing = str(harga)
        print(type(hargaparsing))
        print(type(harga))
        return f"Transaksinya Ber prodak {prodak} dan {hargaparsing}"
    except:
        return f"Transaksinya Ber prodak {prodak} dan {hargaparsing}"


@aplication.get("/transaksi/{detail_transaksi}")
def get_detail():
    transaksi_info = get_transaksi(prodak="kosmetik" , harga="3000")  
    return f"Transaksi yang sudah masuk: {transaksi_info}"


@aplication.post("/transaksi/{insert}")

def insert(InputTransaksi:InputTransaksi):
    transaksi_detaill.append(InputTransaksi)
    return transaksi_detaill
    


