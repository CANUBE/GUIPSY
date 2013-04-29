<html><head></head><body><h2>POTENTIAL</h2> <p>The QIODevice class is the base interface class of all I/O devices in Qt.</p><p>QIODevice provides both a common implementation and an abstract interface for devices that support reading and writing of blocks of data, such as <a href="qfile.html">QFile</a>, <a href="qbuffer.html">QBuffer</a> and <a href="qtcpsocket.html">QTcpSocket</a>. QIODevice is abstract and can not be instantiated, but it is common to use the interface it defines to provide device-independent I/O features. For example, Qts XML classes operate on a QIODevice pointer, allowing them to be used with various devices (such as files and buffers).</p><p>Before accessing the device, <a href="qiodevice.html#open">open</a>() must be called to set the correct <a href="qiodevice.html#OpenModeFlag-enum">OpenMode</a> (such as <a href="qiodevice.html#OpenModeFlag-enum">ReadOnly</a> or <a href="qiodevice.html#OpenModeFlag-enum">ReadWrite</a>). You can then write to the device with <a href="qiodevice.html#write">write</a>() or <a href="qiodevice.html#putChar">putChar</a>(), and read by calling either <a href="qiodevice.html#read">read</a>(), <a href="qiodevice.html#readLine">readLine</a>(), or <a href="qiodevice.html#readAll">readAll</a>(). Call <a href="qiodevice.html#close">close</a>() when you are done with the device.</p><p>QIODevice distinguishes between two types of devices: random-access devices and sequential devices.</p><ul><li>Random-access devices support seeking to arbitrary positions using <a href="qiodevice.html#seek">seek</a>(). The current position in the file is available by calling <a href="qiodevice.html#pos">pos</a>(). <a href="qfile.html">QFile</a> and <a href="qbuffer.html">QBuffer</a> are examples of random-access devices.</li><li>Sequential devices dont support seeking to arbitrary positions. The data must be read in one pass. The functions <a href="qiodevice.html#pos">pos</a>() and <a href="qiodevice.html#size">size</a>() dont work for sequential devices. <a href="qtcpsocket.html">QTcpSocket</a> and <a href="qprocess.html">QProcess</a> are examples of sequential devices.</li></ul></body></html>