#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <store.h>
#include <store_model.h>
#include <QMetaType>

Q_DECLARE_METATYPE(Store);
Q_DECLARE_METATYPE(std::vector<std::string>);

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE



class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    std::vector<Store> readCSV(QString csvFile);
    void setupProxyModel();
    ~MainWindow();

private slots:
    void on_pushButton_5_clicked();

private:
    Ui::MainWindow *ui;
    StoreModel *mModel;
};
#endif // MAINWINDOW_H
