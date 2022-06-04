#include "store_model.h"


StoreModel::StoreModel(QObject *parent, const std::vector<Store> &data)
    : QAbstractTableModel(parent) {
    for(auto s: data)
        stores[s.randomNumber()] = s;
}


int StoreModel::rowCount(const QModelIndex &parent) const {
    return stores.size();
}

int StoreModel::columnCount(const QModelIndex &parent) const {
    return (int)StoreColumns::COUNT;
}

QVariant StoreModel::data(const QModelIndex &index, int role) const {
    if (role == Qt::DisplayRole || role == Qt::EditRole)
    {
        auto it = stores.begin();
        for (int i = 0; i < index.row(); ++i)
            ++it;

        const Store &store = it->second;
        return store.data[index.column()];
    }

    return {};
}

bool StoreModel::setData(const QModelIndex &index, const QVariant &value, int role)
{
    if (role == Qt::EditRole) {
        auto it = stores.begin();
        for (int i = 0; i < index.row(); ++i)
            ++it;

        it->second.data[index.column()] = value;
        return true;
    }

    return false;
}

void StoreModel::insertData(Store curr)
{
    stores[curr.randomNumber()] = curr;
    emit layoutChanged();
}

void StoreModel::deleteData(int pos)
{
    auto it = stores.begin();
    for (int i = 0; i < pos; ++i)
        ++it;

    if (pos >= 0 && pos < (int)stores.size())
            stores.erase(it);


    emit layoutChanged();

}

QVariant StoreModel::headerData(int section, Qt::Orientation orientation, int role) const {
    if (role == Qt::DisplayRole || orientation == Qt::Horizontal)
    {
        StoreColumns column = (StoreColumns)section;
        switch (column) {
        case StoreColumns::storeId:
            return "Store ID";
        case StoreColumns::storeArea:
            return "Store Area";
        case StoreColumns::itemsAvailable:
            return "Items Available";
        case StoreColumns::daylyCustomers:
            return "Daily Customer Count";
        case StoreColumns::storeSales:
            return "Store Sales";
        case StoreColumns::COUNT:
            return {};
        }
    }
    return {};
}

































