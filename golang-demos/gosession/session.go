package main

import (
	"fmt"
)

type Session interface {
	Set(key, value interface{}) error
	Get(key interface{}) interface{}
	Delete(key interface{}) error
	SessionID() string
}

type SessionStore interface {
	SessionInit(sid string) (Session, error)
	SessionGet(sid string) (Session, error)
	SessionDestory(sid string) error
	SessionGC(maxLifeTime int64)
}

type Manager struct {
	cookieName  string
	lock        sync.Mutex
	provider    Provider
	maxlifetime int64
}

func NewManager(provideName)

func main() {

}
