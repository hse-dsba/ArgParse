#ifndef STORE_MODEL_H
#define STORE_MODEL_H


#include <QAbstractTableModel>
#include <QObject>
#include "store.h"
#include <map>

class StoreModel : public QAbstractTableModel {
public:
    std::map<size_t, Store> stores;
    Store *selectedStore = new Store();
    bool hasSelectedStore = false;

    StoreModel(QObject *parent, const std::vector<Store> &data);




    int rowCount(const QModelIndex &parent = QModelIndex()) const override;

    int columnCount(const QModelIndex &parent = QModelIndex()) const override;

    bool setData(const QModelIndex &index, const QVariant &value, int role = Qt::EditRole) override;

    void insertData(Store curr);

    void deleteData(int pos);

    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;

    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override;
};


#endif // STORE_MODEL_H
