constante=1024
def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para byte')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

def byteParaKB(valorASerConvertido):
    print('Valor convertido de byte para KB')
    KBCalculado = valorASerConvertido / constante
    return KBCalculado

def KBParaByte(valorASerConvertido):
    print('Valor convertido de KB para byte')
    ByteCalculado = valorASerConvertido * constante
    return ByteCalculado

def KBParaMB(valorASerConvertido):
    print('Valor convertido de KB para MB')
    MBCalculado = valorASerConvertido / constante
    return MBCalculado

def MBParaKB(valorASerConvertido):
    print('Valor convertido de MB para KB')
    KBCalculado = valorASerConvertido * constante
    return KBCalculado

def MBParaGB(valorASerConvertido):
    print('Valor convertido de MB para GB')
    GBCalculado = valorASerConvertido / constante
    return GBCalculado

def GBParaMB(valorASerConvertido):
    print('Valor convertido de GB para MB')
    MBCalculado = valorASerConvertido * constante
    return MBCalculado

def GBParaTB(valorASerConvertido):
    print('Valor convertido de GB para TB')
    TBCalculado = valorASerConvertido / constante
    return TBCalculado

def TBParaGB(valorASerConvertido):
    print('Valor convertido de TB para GB')
    GB2Calculado = valorASerConvertido / constante
    return GB2Calculado

def TBParaPB(valorASerConvertido):
    print('Valor convertido de TB para PB')
    PBCalculado = valorASerConvertido / constante
    return PBCalculado

def PBParaTB(valorASerConvertido):
    print('Valor convertido de PB para TB')
    TBCalculado = valorASerConvertido * constante
    return TBCalculado

