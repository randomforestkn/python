# /********************************************************************************
# ** Form generated from reading UI file 'interfacex17695.ui'
# **
# ** Created by: Qt User Interface Compiler version 5.9.5
# **
# ** WARNING! All changes made in this file will be lost when recompiling UI file!
# ********************************************************************************/

#ifndef INTERFACEX17695_H
#define INTERFACEX17695_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QToolBox>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QHBoxLayout *horizontalLayout;
    QFrame *slide_menu_container;
    QVBoxLayout *verticalLayout_2;
    QFrame *slide_menu;
    QVBoxLayout *verticalLayout_5;
    QFrame *frame_7;
    QHBoxLayout *horizontalLayout_8;
    QLabel *label_2;
    QLabel *label_3;
    QFrame *frame_8;
    QVBoxLayout *verticalLayout_6;
    QToolBox *toolBox;
    QWidget *page;
    QVBoxLayout *verticalLayout_7;
    QFrame *frame_10;
    QVBoxLayout *verticalLayout_8;
    QPushButton *pushButton_10;
    QPushButton *pushButton_11;
    QPushButton *pushButton_12;
    QWidget *page_2;
    QVBoxLayout *verticalLayout_9;
    QFrame *frame_11;
    QVBoxLayout *verticalLayout_10;
    QPushButton *pushButton_13;
    QPushButton *pushButton_14;
    QLabel *label_4;
    QFrame *frame_9;
    QHBoxLayout *horizontalLayout_9;
    QPushButton *pushButton_9;
    QFrame *main_body;
    QVBoxLayout *verticalLayout;
    QFrame *header_frame;
    QHBoxLayout *horizontalLayout_2;
    QFrame *frame_5;
    QHBoxLayout *horizontalLayout_7;
    QPushButton *pushButton_8;
    QFrame *frame_3;
    QHBoxLayout *horizontalLayout_6;
    QLineEdit *lineEdit;
    QPushButton *pushButton_6;
    QFrame *frame_2;
    QHBoxLayout *horizontalLayout_5;
    QPushButton *pushButton_5;
    QPushButton *pushButton_4;
    QFrame *frame;
    QHBoxLayout *horizontalLayout_4;
    QPushButton *pushButton_3;
    QPushButton *pushButton_2;
    QPushButton *pushButton;
    QFrame *main_body_contents;
    QVBoxLayout *verticalLayout_11;
    QLabel *label_6;
    QLabel *label_5;
    QFrame *footer;
    QHBoxLayout *horizontalLayout_3;
    QFrame *frame_4;
    QVBoxLayout *verticalLayout_4;
    QLabel *label;
    QFrame *frame_6;
    QVBoxLayout *verticalLayout_3;
    QPushButton *pushButton_7;
    QFrame *size_grip;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(766, 600);
        MainWindow->setStyleSheet(QLatin1String("*{\n"
"	border: none;\n"
"}"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        centralwidget->setStyleSheet(QStringLiteral("background-color: rgb(24, 24, 36);"));
        horizontalLayout = new QHBoxLayout(centralwidget);
        horizontalLayout->setSpacing(0);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        slide_menu_container = new QFrame(centralwidget);
        slide_menu_container->setObjectName(QStringLiteral("slide_menu_container"));
        slide_menu_container->setMaximumSize(QSize(0, 16777215));
        slide_menu_container->setStyleSheet(QStringLiteral("background-color: rgb(9, 5, 13);"));
        slide_menu_container->setFrameShape(QFrame::StyledPanel);
        slide_menu_container->setFrameShadow(QFrame::Raised);
        verticalLayout_2 = new QVBoxLayout(slide_menu_container);
        verticalLayout_2->setSpacing(0);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        slide_menu = new QFrame(slide_menu_container);
        slide_menu->setObjectName(QStringLiteral("slide_menu"));
        slide_menu->setMinimumSize(QSize(192, 0));
        slide_menu->setFrameShape(QFrame::StyledPanel);
        slide_menu->setFrameShadow(QFrame::Raised);
        verticalLayout_5 = new QVBoxLayout(slide_menu);
        verticalLayout_5->setSpacing(0);
        verticalLayout_5->setObjectName(QStringLiteral("verticalLayout_5"));
        verticalLayout_5->setContentsMargins(0, 0, 0, 0);
        frame_7 = new QFrame(slide_menu);
        frame_7->setObjectName(QStringLiteral("frame_7"));
        frame_7->setFrameShape(QFrame::StyledPanel);
        frame_7->setFrameShadow(QFrame::Raised);
        horizontalLayout_8 = new QHBoxLayout(frame_7);
        horizontalLayout_8->setObjectName(QStringLiteral("horizontalLayout_8"));
        label_2 = new QLabel(frame_7);
        label_2->setObjectName(QStringLiteral("label_2"));
        QFont font;
        font.setPointSize(12);
        font.setBold(true);
        font.setWeight(75);
        label_2->setFont(font);

        horizontalLayout_8->addWidget(label_2, 0, Qt::AlignLeft|Qt::AlignTop);

        label_3 = new QLabel(frame_7);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setPixmap(QPixmap(QString::fromUtf8(":/icons/icons/codesandbox.svg")));

        horizontalLayout_8->addWidget(label_3, 0, Qt::AlignLeft|Qt::AlignTop);


        verticalLayout_5->addWidget(frame_7, 0, Qt::AlignTop);

        frame_8 = new QFrame(slide_menu);
        frame_8->setObjectName(QStringLiteral("frame_8"));
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(frame_8->sizePolicy().hasHeightForWidth());
        frame_8->setSizePolicy(sizePolicy);
        frame_8->setFrameShape(QFrame::StyledPanel);
        frame_8->setFrameShadow(QFrame::Raised);
        verticalLayout_6 = new QVBoxLayout(frame_8);
        verticalLayout_6->setSpacing(0);
        verticalLayout_6->setObjectName(QStringLiteral("verticalLayout_6"));
        verticalLayout_6->setContentsMargins(0, 0, 0, 0);
        toolBox = new QToolBox(frame_8);
        toolBox->setObjectName(QStringLiteral("toolBox"));
        toolBox->setStyleSheet(QLatin1String("QToolBox{\n"
"	background-color: rgb(24, 24, 36);\n"
"	text-align: left;\n"
"}\n"
"QToolBox::tab{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(17, 16, 26);\n"
"	text-align: left;\n"
"}"));
        page = new QWidget();
        page->setObjectName(QStringLiteral("page"));
        page->setGeometry(QRect(0, 0, 86, 51));
        verticalLayout_7 = new QVBoxLayout(page);
        verticalLayout_7->setSpacing(0);
        verticalLayout_7->setObjectName(QStringLiteral("verticalLayout_7"));
        verticalLayout_7->setContentsMargins(0, 0, 0, 0);
        frame_10 = new QFrame(page);
        frame_10->setObjectName(QStringLiteral("frame_10"));
        frame_10->setFrameShape(QFrame::StyledPanel);
        frame_10->setFrameShadow(QFrame::Raised);
        verticalLayout_8 = new QVBoxLayout(frame_10);
        verticalLayout_8->setSpacing(0);
        verticalLayout_8->setObjectName(QStringLiteral("verticalLayout_8"));
        verticalLayout_8->setContentsMargins(0, 0, 0, 0);
        pushButton_10 = new QPushButton(frame_10);
        pushButton_10->setObjectName(QStringLiteral("pushButton_10"));
        QIcon icon;
        icon.addFile(QStringLiteral(":/icons/icons/watch.svg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_10->setIcon(icon);
        pushButton_10->setIconSize(QSize(16, 16));

        verticalLayout_8->addWidget(pushButton_10);

        pushButton_11 = new QPushButton(frame_10);
        pushButton_11->setObjectName(QStringLiteral("pushButton_11"));
        QIcon icon1;
        icon1.addFile(QStringLiteral(":/icons/icons/book.svg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_11->setIcon(icon1);

        verticalLayout_8->addWidget(pushButton_11);

        pushButton_12 = new QPushButton(frame_10);
        pushButton_12->setObjectName(QStringLiteral("pushButton_12"));
        QIcon icon2;
        icon2.addFile(QStringLiteral(":/icons/icons/database.svg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_12->setIcon(icon2);

        verticalLayout_8->addWidget(pushButton_12);


        verticalLayout_7->addWidget(frame_10, 0, Qt::AlignTop);

        QIcon icon3;
        icon3.addFile(QStringLiteral(":/icons/icons/chevron-down.svg"), QSize(), QIcon::Normal, QIcon::Off);
        toolBox->addItem(page, icon3, QStringLiteral("Drop Menu 1"));
        page_2 = new QWidget();
        page_2->setObjectName(QStringLiteral("page_2"));
        page_2->setGeometry(QRect(0, 0, 192, 477));
        verticalLayout_9 = new QVBoxLayout(page_2);
        verticalLayout_9->setSpacing(0);
        verticalLayout_9->setObjectName(QStringLiteral("verticalLayout_9"));
        verticalLayout_9->setContentsMargins(0, 0, 0, 0);
        frame_11 = new QFrame(page_2);
        frame_11->setObjectName(QStringLiteral("frame_11"));
        frame_11->setFrameShape(QFrame::StyledPanel);
        frame_11->setFrameShadow(QFrame::Raised);
        verticalLayout_10 = new QVBoxLayout(frame_11);
        verticalLayout_10->setSpacing(0);
        verticalLayout_10->setObjectName(QStringLiteral("verticalLayout_10"));
        verticalLayout_10->setContentsMargins(0, 0, 0, 0);
        pushButton_13 = new QPushButton(frame_11);
        pushButton_13->setObjectName(QStringLiteral("pushButton_13"));
        QIcon icon4;
        icon4.addFile(QStringLiteral(":/icons/icons/phone-call.svg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_13->setIcon(icon4);

        verticalLayout_10->addWidget(pushButton_13);

        pushButton_14 = new QPushButton(frame_11);
        pushButton_14->setObjectName(QStringLiteral("pushButton_14"));
        QIcon icon5;
        icon5.addFile(QStringLiteral(":/icons/icons/mail.svg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_14->setIcon(icon5);

        verticalLayout_10->addWidget(pushButton_14);


        verticalLayout_9->addWidget(frame_11, 0, Qt::AlignTop);

        label_4 = new QLabel(page_2);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setWordWrap(true);

        verticalLayout_9->addWidget(label_4, 0, Qt::AlignTop);

        toolBox->addItem(page_2, icon3, QStringLiteral("Drop Menu 2"));

        verticalLayout_6->addWidget(toolBox);


        verticalLayout_5->addWidget(frame_8);

        frame_9 = new QFrame(slide_menu);
        frame_9->setObjectName(QStringLiteral("frame_9"));
        frame_9->setFrameShape(QFrame::StyledPanel);
        frame_9->setFrameShadow(QFrame::Raised);
        horizontalLayout_9 = new QHBoxLayout(frame_9);
        horizontalLayout_9->setSpacing(0);
        horizontalLayout_9->setObjectName(QStringLiteral("horizontalLayout_9"));
        horizontalLayout_9->setContentsMargins(0, 0, 0, 0);
        pushButton_9 = new QPushButton(frame_9);
        pushButton_9->setObjectName(QStringLiteral("pushButton_9"));
        QIcon icon6;
        icon6.addFile(QStringLiteral(":/icons/icons/external-link.svg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_9->setIcon(icon6);
        pushButton_9->setIconSize(QSize(16, 16));

        horizontalLayout_9->addWidget(pushButton_9, 0, Qt::AlignLeft|Qt::AlignBottom);


        verticalLayout_5->addWidget(frame_9, 0, Qt::AlignBottom);


        verticalLayout_2->addWidget(slide_menu);


        horizontalLayout->addWidget(slide_menu_container);

        main_body = new QFrame(centralwidget);
        main_body->setObjectName(QStringLiteral("main_body"));
        main_body->setFrameShape(QFrame::StyledPanel);
        main_body->setFrameShadow(QFrame::Raised);
        verticalLayout = new QVBoxLayout(main_body);
        verticalLayout->setSpacing(0);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        header_frame = new QFrame(main_body);
        header_frame->setObjectName(QStringLiteral("header_frame"));
        header_frame->setStyleSheet(QStringLiteral("background-color: rgb(9, 5, 13);"));
        header_frame->setFrameShape(QFrame::StyledPanel);
        header_frame->setFrameShadow(QFrame::Raised);
        horizontalLayout_2 = new QHBoxLayout(header_frame);
        horizontalLayout_2->setSpacing(0);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        frame_5 = new QFrame(header_frame);
        frame_5->setObjectName(QStringLiteral("frame_5"));
        frame_5->setFrameShape(QFrame::StyledPanel);
        frame_5->setFrameShadow(QFrame::Raised);
        horizontalLayout_7 = new QHBoxLayout(frame_5);
        horizontalLayout_7->setSpacing(6);
        horizontalLayout_7->setObjectName(QStringLiteral("horizontalLayout_7"));
        horizontalLayout_7->setContentsMargins(6, 6, 6, 6);
        pushButton_8 = new QPushButton(frame_5);
        pushButton_8->setObjectName(QStringLiteral("pushButton_8"));
        QIcon icon7;
        icon7.addFile(QStringLiteral(":/icons/icons/align-justify.svg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_8->setIcon(icon7);
        pushButton_8->setIconSize(QSize(32, 32));

        horizontalLayout_7->addWidget(pushButton_8, 0, Qt::AlignLeft|Qt::AlignTop);


        horizontalLayout_2->addWidget(frame_5, 0, Qt::AlignLeft|Qt::AlignTop);

        frame_3 = new QFrame(header_frame);
        frame_3->setObjectName(QStringLiteral("frame_3"));
        frame_3->setFrameShape(QFrame::StyledPanel);
        frame_3->setFrameShadow(QFrame::Raised);
        horizontalLayout_6 = new QHBoxLayout(frame_3);
        horizontalLayout_6->setSpacing(6);
        horizontalLayout_6->setObjectName(QStringLiteral("horizontalLayout_6"));
        horizontalLayout_6->setContentsMargins(6, 6, 6, 6);
        lineEdit = new QLineEdit(frame_3);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));
        lineEdit->setMinimumSize(QSize(120, 0));
        lineEdit->setStyleSheet(QStringLiteral("border-bottom: 3px solid rgb(230,5,64);"));

        horizontalLayout_6->addWidget(lineEdit, 0, Qt::AlignLeft|Qt::AlignTop);

        pushButton_6 = new QPushButton(frame_3);
        pushButton_6->setObjectName(QStringLiteral("pushButton_6"));
        QIcon icon8;
        icon8.addFile(QStringLiteral(":/icons/icons/search.svg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_6->setIcon(icon8);

        horizontalLayout_6->addWidget(pushButton_6, 0, Qt::AlignLeft|Qt::AlignTop);


        horizontalLayout_2->addWidget(frame_3, 0, Qt::AlignLeft|Qt::AlignTop);

        frame_2 = new QFrame(header_frame);
        frame_2->setObjectName(QStringLiteral("frame_2"));
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        horizontalLayout_5 = new QHBoxLayout(frame_2);
        horizontalLayout_5->setSpacing(6);
        horizontalLayout_5->setObjectName(QStringLiteral("horizontalLayout_5"));
        horizontalLayout_5->setContentsMargins(6, 6, 6, 6);
        pushButton_5 = new QPushButton(frame_2);
        pushButton_5->setObjectName(QStringLiteral("pushButton_5"));
        QIcon icon9;
        icon9.addFile(QStringLiteral(":/icons/icons/user.svg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_5->setIcon(icon9);

        horizontalLayout_5->addWidget(pushButton_5);

        pushButton_4 = new QPushButton(frame_2);
        pushButton_4->setObjectName(QStringLiteral("pushButton_4"));
        QIcon icon10;
        icon10.addFile(QStringLiteral(":/icons/icons/bell.svg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_4->setIcon(icon10);

        horizontalLayout_5->addWidget(pushButton_4);


        horizontalLayout_2->addWidget(frame_2, 0, Qt::AlignHCenter|Qt::AlignTop);

        frame = new QFrame(header_frame);
        frame->setObjectName(QStringLiteral("frame"));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        horizontalLayout_4 = new QHBoxLayout(frame);
        horizontalLayout_4->setSpacing(6);
        horizontalLayout_4->setObjectName(QStringLiteral("horizontalLayout_4"));
        horizontalLayout_4->setContentsMargins(6, 6, 6, 6);
        pushButton_3 = new QPushButton(frame);
        pushButton_3->setObjectName(QStringLiteral("pushButton_3"));
        QIcon icon11;
        icon11.addFile(QStringLiteral(":/icons/icons/arrow-down-left.svg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_3->setIcon(icon11);

        horizontalLayout_4->addWidget(pushButton_3);

        pushButton_2 = new QPushButton(frame);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));
        QIcon icon12;
        icon12.addFile(QStringLiteral(":/icons/icons/maximize-2.svg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_2->setIcon(icon12);

        horizontalLayout_4->addWidget(pushButton_2);

        pushButton = new QPushButton(frame);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        QIcon icon13;
        icon13.addFile(QStringLiteral(":/icons/icons/x.svg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton->setIcon(icon13);

        horizontalLayout_4->addWidget(pushButton);


        horizontalLayout_2->addWidget(frame, 0, Qt::AlignRight|Qt::AlignTop);


        verticalLayout->addWidget(header_frame, 0, Qt::AlignTop);

        main_body_contents = new QFrame(main_body);
        main_body_contents->setObjectName(QStringLiteral("main_body_contents"));
        sizePolicy.setHeightForWidth(main_body_contents->sizePolicy().hasHeightForWidth());
        main_body_contents->setSizePolicy(sizePolicy);
        main_body_contents->setFrameShape(QFrame::StyledPanel);
        main_body_contents->setFrameShadow(QFrame::Raised);
        verticalLayout_11 = new QVBoxLayout(main_body_contents);
        verticalLayout_11->setObjectName(QStringLiteral("verticalLayout_11"));
        label_6 = new QLabel(main_body_contents);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setMinimumSize(QSize(40, 40));
        label_6->setMaximumSize(QSize(40, 40));
        label_6->setStyleSheet(QLatin1String("border: 3px solid rgb(230, 5, 64);\n"
"border-radius: 20px;"));
        label_6->setPixmap(QPixmap(QString::fromUtf8(":/icons/icons/chrome.svg")));
        label_6->setAlignment(Qt::AlignCenter);

        verticalLayout_11->addWidget(label_6, 0, Qt::AlignHCenter|Qt::AlignBottom);

        label_5 = new QLabel(main_body_contents);
        label_5->setObjectName(QStringLiteral("label_5"));
        QFont font1;
        font1.setPointSize(20);
        font1.setBold(true);
        font1.setWeight(75);
        label_5->setFont(font1);

        verticalLayout_11->addWidget(label_5, 0, Qt::AlignHCenter|Qt::AlignTop);


        verticalLayout->addWidget(main_body_contents);

        footer = new QFrame(main_body);
        footer->setObjectName(QStringLiteral("footer"));
        footer->setFrameShape(QFrame::StyledPanel);
        footer->setFrameShadow(QFrame::Raised);
        horizontalLayout_3 = new QHBoxLayout(footer);
        horizontalLayout_3->setSpacing(0);
        horizontalLayout_3->setObjectName(QStringLiteral("horizontalLayout_3"));
        horizontalLayout_3->setContentsMargins(0, 0, 0, 0);
        frame_4 = new QFrame(footer);
        frame_4->setObjectName(QStringLiteral("frame_4"));
        frame_4->setFrameShape(QFrame::StyledPanel);
        frame_4->setFrameShadow(QFrame::Raised);
        verticalLayout_4 = new QVBoxLayout(frame_4);
        verticalLayout_4->setSpacing(0);
        verticalLayout_4->setObjectName(QStringLiteral("verticalLayout_4"));
        verticalLayout_4->setContentsMargins(0, 0, 0, 0);
        label = new QLabel(frame_4);
        label->setObjectName(QStringLiteral("label"));

        verticalLayout_4->addWidget(label, 0, Qt::AlignBottom);


        horizontalLayout_3->addWidget(frame_4);

        frame_6 = new QFrame(footer);
        frame_6->setObjectName(QStringLiteral("frame_6"));
        frame_6->setFrameShape(QFrame::StyledPanel);
        frame_6->setFrameShadow(QFrame::Raised);
        verticalLayout_3 = new QVBoxLayout(frame_6);
        verticalLayout_3->setSpacing(0);
        verticalLayout_3->setObjectName(QStringLiteral("verticalLayout_3"));
        verticalLayout_3->setContentsMargins(0, 0, 0, 0);
        pushButton_7 = new QPushButton(frame_6);
        pushButton_7->setObjectName(QStringLiteral("pushButton_7"));
        QIcon icon14;
        icon14.addFile(QStringLiteral(":/icons/icons/box.svg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_7->setIcon(icon14);

        verticalLayout_3->addWidget(pushButton_7, 0, Qt::AlignBottom);


        horizontalLayout_3->addWidget(frame_6);

        size_grip = new QFrame(footer);
        size_grip->setObjectName(QStringLiteral("size_grip"));
        size_grip->setMinimumSize(QSize(10, 10));
        size_grip->setMaximumSize(QSize(10, 10));
        size_grip->setFrameShape(QFrame::StyledPanel);
        size_grip->setFrameShadow(QFrame::Raised);

        horizontalLayout_3->addWidget(size_grip, 0, Qt::AlignRight|Qt::AlignBottom);


        verticalLayout->addWidget(footer, 0, Qt::AlignBottom);


        horizontalLayout->addWidget(main_body);

        MainWindow->setCentralWidget(centralwidget);

        retranslateUi(MainWindow);

        toolBox->setCurrentIndex(1);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", Q_NULLPTR));
        label_2->setText(QApplication::translate("MainWindow", "MY APP", Q_NULLPTR));
        label_3->setText(QString());
        pushButton_10->setText(QApplication::translate("MainWindow", "ITEM 1", Q_NULLPTR));
        pushButton_11->setText(QApplication::translate("MainWindow", "ITEM 2", Q_NULLPTR));
        pushButton_12->setText(QApplication::translate("MainWindow", "ITEM 3", Q_NULLPTR));
        toolBox->setItemText(toolBox->indexOf(page), QApplication::translate("MainWindow", "Drop Menu 1", Q_NULLPTR));
        pushButton_13->setText(QApplication::translate("MainWindow", "SUB MENU", Q_NULLPTR));
        pushButton_14->setText(QApplication::translate("MainWindow", "SUBMENU", Q_NULLPTR));
        label_4->setText(QApplication::translate("MainWindow", "Some Text to fill here", Q_NULLPTR));
        toolBox->setItemText(toolBox->indexOf(page_2), QApplication::translate("MainWindow", "Drop Menu 2", Q_NULLPTR));
        pushButton_9->setText(QApplication::translate("MainWindow", "Exit", Q_NULLPTR));
        pushButton_8->setText(QString());
        lineEdit->setPlaceholderText(QApplication::translate("MainWindow", "Search", Q_NULLPTR));
        pushButton_6->setText(QString());
        pushButton_5->setText(QString());
        pushButton_4->setText(QString());
        pushButton_3->setText(QString());
        pushButton_2->setText(QString());
        pushButton->setText(QString());
        label_6->setText(QString());
        label_5->setText(QApplication::translate("MainWindow", "DATABASE", Q_NULLPTR));
        label->setText(QApplication::translate("MainWindow", "Modern UI", Q_NULLPTR));
        pushButton_7->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // INTERFACEX17695_H
