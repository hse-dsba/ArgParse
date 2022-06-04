#include <unordered_set>
#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <QString>
#include <QFileDialog>
#include "store.h"
#include "rapidcsv.h"
#include "store_model.h"
#include <QList>






MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
//    std::vector<Store> readCSV;
//    mModel = new StoreModel();
//    ui->tableView->setModel(mModel);
}

MainWindow::~MainWindow()
{
    delete ui;
}


std::vector<Store> MainWindow::readCSV(QString csvFile)
{
    rapidcsv::Document doc(csvFile.toStdString());

    int numOfRows = doc.GetRowCount();
    std::vector<QVariant> modelRow;
    std::vector<std::string> row;
    std::vector<Store> modelData;
    std::vector<QVariant> kk;
    for (int rownum = 0; rownum < numOfRows; ++rownum)
    {
        row = doc.GetRow<std::string>(rownum);
        Store curr({QString::fromStdString(row[0]), QString::fromStdString(row[1]), QString::fromStdString(row[2]), QString::fromStdString(row[3]), QString::fromStdString(row[4])});
        modelData.push_back(curr);
    }


    std::vector<Store> result;

    for (auto curr: modelData)
        result.push_back(curr);


    return result;
}




void MainWindow::on_pushButton_5_clicked()
{
    QString filename = QFileDialog::getOpenFileName(this, "Open file", QDir::currentPath(), "CSV File(*.csv)");

    StoreModel model(this, readCSV(filename));

    ui->tableView->setModel(&model);
    setCentralWidget(ui->tableView);

}

