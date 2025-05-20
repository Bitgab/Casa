-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Paciente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Paciente` (
  `IdPaciente` INT NOT NULL AUTO_INCREMENT,
  `PrimeiroNomePaciente` VARCHAR(20) NULL,
  `NomeDoMeioPaciente` VARCHAR(20) NULL,
  `UltimoNomePaciente` VARCHAR(20) NULL,
  `CPF` VARCHAR(14) NOT NULL,
  `DDD` VARCHAR(3) NULL,
  `NumTelefone` VARCHAR(10) NULL,
  PRIMARY KEY (`IdPaciente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Medico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Medico` (
  `idMedico` INT NOT NULL AUTO_INCREMENT,
  `CRM` VARCHAR(20) NOT NULL,
  `PrimeiroNomeMedico` VARCHAR(20) NULL,
  `NomeDoMeioMedico` VARCHAR(20) NULL,
  `UltimoNomeMEdico` VARCHAR(20) NULL,
  `Especializaçãol` VARCHAR(20) NULL,
  PRIMARY KEY (`idMedico`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Consulta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Consulta` (
  `idConsulta` INT NOT NULL,
  `Data` DATE NOT NULL,
  `Hora` TIME NOT NULL,
  `Observação` VARCHAR(80) NULL,
  `Paciente_IdPaciente` INT NOT NULL,
  `Medico_idMedico` INT NOT NULL,
  PRIMARY KEY (`idConsulta`, `Paciente_IdPaciente`, `Medico_idMedico`),
  INDEX `fk_Consulta_Paciente_idx` (`Paciente_IdPaciente` ASC) VISIBLE,
  INDEX `fk_Consulta_Medico1_idx` (`Medico_idMedico` ASC) VISIBLE,
  CONSTRAINT `fk_Consulta_Paciente`
    FOREIGN KEY (`Paciente_IdPaciente`)
    REFERENCES `mydb`.`Paciente` (`IdPaciente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Consulta_Medico1`
    FOREIGN KEY (`Medico_idMedico`)
    REFERENCES `mydb`.`Medico` (`idMedico`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
