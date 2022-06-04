#ifndef STORE_H
#define STORE_H

#include <QVariant>
#include <vector>

enum class StoreColumns {
    storeId,
    storeArea,
    itemsAvailable,
    daylyCustomers,
    storeSales,
    COUNT
};

class Store {
public:
    Store(const std::vector<QVariant> &data);

    Store();

    std::vector<QVariant> data;

    int storeId() const;

    int randomNumber() const;

    int storeArea() const;

    int itemsAvailable() const;

    int daylyCustomers() const;

    int storeSales() const;

};

#endif // STORE_H
