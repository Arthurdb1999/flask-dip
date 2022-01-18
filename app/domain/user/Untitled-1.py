class VendaItem():
    pass

class Venda():
    self.__venda_item: VendaItem
    def adicionar_item(self, item: VendaItem)
        pass

unitOfWork.BeginTransaction()
try
    executa_venda()
    unitOfWork.CommitTransaction()    
except
    unitOfWork.Rollback()


def executa_venda()
    venda = Venda()
    venda.adicionar_item(VendaItem(...))
    for item in Venda.Items:
        estoque.upate_qtd(item.produto, item.qtd);
    repository.add(venda)






class EstoqueService():
    def updateQtd(self, produto: Produto, novaQtd: int):
        pass